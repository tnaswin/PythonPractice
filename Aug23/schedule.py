from twisted.internet import reactor
from twisted.python import log
import sys, time
from twisted.internet.task import LoopingCall, deferLater

log.startLogging(sys.stdout)

iterVal = 0

def loopedFunction():
    global iterVal
    iterVal = iterVal + 1
    now = time.localtime(time.time())
    timeStr = str(time.strftime("%y/%m/%d %H:%M:%S",now))
    log.msg(timeStr + " : iteration : " + str(iterVal))

def cancelLoop(loopObj):
    log.msg("Called cancelLoop")
    loopObj.stop()
    log.msg("Loop object has been stopped")
    log.msg("Shutting down the reactor")
    reactor.stop()

now = time.localtime(time.time())
timeStr = str(time.strftime("%y/%m/%d %H:%M:%S",now))
log.msg(timeStr)
log.msg("will call loopedFunction, every 2 second")

loopObj = LoopingCall(loopedFunction)
loopObj.start(2, now=True)

defObj = deferLater(reactor, 8, cancelLoop, loopObj)
# We could also have used callLater
#reactor.callLater(8, cancelLoop, loopObj)
reactor.run()
