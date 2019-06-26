import sys
from twisted.internet import reactor
from twisted.python import log
log.startLogging(sys.stdout)

def callfunc(x):
    log.msg("In callfunc as event handler")
    log.msg(str(x))
    log.msg("Will shut down")
    reactor.stop()

reactor.callWhenRunning(callfunc, "This was passed to callfunc")
reactor.run()
