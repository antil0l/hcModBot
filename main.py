import coreFunctions
import commands


ws = coreFunctions.wscon()
coreFunctions.joinChannel(ws, 'test')

# the calls in this loop will be on spread threads
while True:
    coreFunctions.currentChat(ws)
    commands.whiteTrips = coreFunctions.whiteTrips
