import json
from tkinter.filedialog import SaveFileDialog
import websocket

userInfo = json.loads(open('info.json', 'r').read())
whiteTrips = []
blackTrips = []

#profiles = list(userInfo['sessions'].keys())
#print('\npossible profiles are: %s' % ', '.join(profiles))


def wscon():
    url = "wss://hack.chat/chat-ws"
    return websocket.create_connection(url, header=["User-Agent: pyain"])


def send_raw(ws, pkg):
    ws.send(json.dumps(pkg))


def joinChannel(ws, session):
    '''
    Description: Join the target channel using the supplied nick and password
        Usage:
            API: { cmd: 'join', nick: '<your nickname>', pass: '<optional password>', channel: '<target channel>' }
    '''
    nick = userInfo[session]['nick']
    password = userInfo[session]['password']
    channel = userInfo[session]['channel']
    send_raw(ws, {'cmd': 'join', 'nick': nick,
             'pass': password, 'channel': channel})
    return onlineSet(server(ws))


def server(ws):
    return json.loads(ws.recv())


def onlineSet(firstMsg):
    online = ', '.join(list(firstMsg['nicks']))
    print(f'- {online} - are online\n')
    for userData in firstMsg['users']:
        if userData['uType'] == 'mod' and userData['trip'] not in whiteTrips:
            whiteTrips.append(userData['trip'])
        if userData['isme'] == True:
            blackTrips.append(userData['nick'])


def onlineAdd(user):
    print(user['nick'], 'joined\n')


def onlineRemove(user):
    print(user['nick'], 'left\n')


def serverInfo(info):
    print(f'INFO :: {info["text"]}\n')


def serverChat(pkg):
    if pkg['nick'] in blackTrips:
        pass
    elif 'trip' in pkg and pkg['trip'] in whiteTrips:
        print(f'-{pkg["trip"]}-#{pkg["nick"]} :: {pkg["text"]}\n')
    elif 'trip' in pkg:
        print(f'{pkg["trip"]}#{pkg["nick"]} :: {pkg["text"]}\n')
    else:
        print(f'NoTrip#{pkg["nick"]} :: {pkg["text"]}\n')


def currentChat(ws):
    serverResponse = server(ws)

    if serverResponse['cmd'] == 'chat':
        serverChat(serverResponse)

    if serverResponse['cmd'] == 'onlineRemove':
        onlineRemove(serverResponse)

    if serverResponse['cmd'] == 'onlineAdd':
        onlineAdd(serverResponse)

    if serverResponse['cmd'] == 'onlineSet':
        onlineSet(serverResponse)

    if serverResponse['cmd'] == 'info':
        serverInfo(serverResponse)


def listener(ws):
    serverResponse = server(ws)
    if serverResponse['cmd'] == 'chat' and serverResponse['text'].startswith(('>', '>?')):
        return True
    else:
        False
