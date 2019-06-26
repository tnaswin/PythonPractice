from twisted.internet import reactor
from twisted.python import log
import sys, time
from string import ascii_lowercase
from twisted.internet.task import cooperate, coiterate
log.startLogging(sys.stdout)

class Counter(object):

    def __init__(self, start, end):
        self.iterVal = start
        self.end = end

    def __iter__(self):
        return self

    def next(self):
        if self.iterVal > self.end:
            raise StopIteration
        else:
            self.iterVal += 1
            return self.iterVal - 1


class AlphaCounter(object):

    def __init__(self, start, end):
        assert(str(start) in ascii_lowercase)
        assert(str(end) in ascii_lowercase)
        assert(ord(str(start)) < ord(str(end)))
        self.iterVal = ord(str(start))
        self.end = ord(str(end))

    def __iter__(self):
        return self

    def next(self):
        if self.iterVal > self.end:
            raise StopIteration
        else:
            self.iterVal += 1
            return chr(self.iterVal - 1)


counterObj = Counter(1,11)
alphaCounterObj = AlphaCounter('d', 'p')

def simplyPrint(data):
    print data

def loopFunction(iterObj):
    for obj in iterObj:
        simplyPrint(obj)

reactor.callWhenRunning(loopFunction, counterObj)
reactor.callWhenRunning(loopFunction, alphaCounterObj)

def loopCooperatively(iterObj):

    def copIterate():
        for obj in iterObj:
            simplyPrint(obj)
            yield None

    return cooperate(copIterate())

task2 = loopCooperatively(AlphaCounter('k', 'z'))
task2_d = task2.whenDone()
task2.pause()
task2.resume()

def simpleIterate(iterObj):
        for obj in iterObj:
            simplyPrint(obj)
            yield None

task3 =  coiterate(simpleIterate(Counter(100,111)))

reactor.run()
