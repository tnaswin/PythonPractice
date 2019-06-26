from twisted.internet import task
from twisted.internet.defer import Deferred
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver


class EchoClient(LineReceiver):

    terminate = "end"

    def connectionMade(self):
        name = raw_input("Enter your name: ")
        age = raw_input("Enter your age: ")
        stop = raw_input("Type 'end' to terminate connection: ")
        data = ",".join([name, str(age), stop])
        self.sendLine(data)

    def lineReceived(self, line):
        l = line.split(",")
        print l[0], l[1]
        if str(l[2]) == self.terminate:
            self.transport.loseConnection()
            return
        name = raw_input("Enter your name: ")
        age = raw_input("Enter your age: ")
        stop = raw_input("Type 'end' to end connection: ")
        data = ",".join([name, str(age), stop])
        self.sendLine(data)


class EchoClientFactory(ClientFactory):


    protocol = EchoClient

    def __init__(self):
        self.done = Deferred()

    def clientConnectionFailed(self, connector, reason):
        print 'connection failed:', reason.getErrorMessage()
        self.done.errback(reason)

    def clientConnectionLost(self, connector, reason):
        print 'connection lost:', reason.getErrorMessage()
        self.done.callback(None)


def main(reactor):
    factory = EchoClientFactory()
    reactor.connectTCP('localhost', 8000, factory)
    return factory.done

if __name__ == '__main__':
    task.react(main)
