import json
import websocket

userInfo = json.loads(open('info.json', 'r').read())
whiteTrips = []
blackedNames = []

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
    for i in firstMsg['users']:
        if i['uType'] == 'mod' and i['trip'] not in whiteTrips:
            whiteTrips.append(i['trip'])
        if i['isme'] == True:
            blackedNames.append(i['nick'])


def onlineAdd(user):
    print(user['nick'], 'joined\n')


def onlineRemove(user):
    print(user['nick'], 'left\n')


def serverInfo(info):
    print(f'INFO :: {info["text"]}\n')


def serverChat(pkg):
    if pkg['nick'] in blackedNames:
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



"""
x{'cmd': 'onlineSet', 'nicks': ['lold', 'test'], 'users': [{'channel': 'bot-test', 'isme': False, 'nick': 'lold', 'trip': 'xhvbdp', 'uType': 'mod', 'hash': 'GxRM5O28hT+PWgV', 'level': 999999, 'userid': 790810229387, 'isBot': False, 'color': False}, {'isme': True, 'isBot': False, 'nick': 'test', 'trip': 'xhvbdp', 'uType': 'mod', 'hash': 'GxRM5O28hT+PWgV', 'level': 999999, 'userid': 5107671142066, 'color': False, 'channel': 'bot-test'}], 'channel': 'bot-test', 'time': 1661181914662}
x{'cmd': 'info', 'text': 'New beta available at: https://beta.hack.chat/ or https://beta.hack.chat/?bot-test', 'channel': 'bot-test', 'time': 1661181914662}
x{'cmd': 'chat', 'nick': 'lold', 'uType': 'mod', 'userid': 790810229387, 'channel': 'bot-test', 'text': 'a', 'level': 999999, 'mod': True, 'trip': 'xhvbdp', 'time': 1661181922935}
x{'cmd': 'onlineRemove', 'userid': 790810229387, 'nick': 'lold', 'channel': 'bot-test', 'time': 1661181933406}
x{'nick': 'pony', 'trip': 'xhvbdp', 'uType': 'mod', 'hash': 'GxRM5O28hT+PWgV', 'level': 999999, 'userid': 790810229387, 'isBot': False, 'color': False, 'cmd': 'onlineAdd', 'channel': 'bot-test', 'time': 1661181933406}
x{'cmd': 'info', 'text': 'lold is now pony', 'channel': 'bot-test', 'time': 1661181933407}
x{'cmd': 'info', 'channel': 'bot-test', 'from': 'pony', 'to': 5107671142066, 'text': 'pony whispered: hi', 'type': 'whisper', 'trip': 'xhvbdp', 'level': 999999, 'uType': 'mod', 'time': 1661181941065}
x{'cmd': 'onlineRemove', 'userid': 790810229387, 'nick': 'pony', 'channel': 'bot-test', 'time': 1661181950465}
x{'cmd': 'onlineAdd', 'nick': 'lold', 'trip': 'xhvbdp', 'uType': 'mod', 'hash': 'GxRM5O28hT+PWgV', 'level': 999999, 'userid': 1690364758913, 'isBot': False, 'color': False, 'channel': 'bot-test', 'time': 1661181961381}
"""
