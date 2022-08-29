import core
import cmd
import threading


ws = core.wscon()
core.joinChannel(ws, 'test')

# the calls in this loop will be on spread threads
while True:
    cmd.whiteTrips = core.whiteTrips
    cmd.blackTrips = core.blackTrips
    core.currentChat(ws)
    if core.listener(ws):
        cmd.handler(core.server(ws)['text'])
