import core
import cmd


ws = core.wscon()
core.joinChannel(ws, 'test')

# the calls in this loop will be on spread threads
while True:
    core.currentChat(ws)
    cmd.whiteTrips = core.whiteTrips
