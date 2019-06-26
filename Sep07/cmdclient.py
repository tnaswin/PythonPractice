from twisted.internet import task
from twisted.internet.defer import Deferred
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver


class EchoClient(LineReceiver):

    terminate = "end"

    def connectionMade(self):
        print "Connection Succesful!\n"
        print "Type 'end' to termiate the program\n"
        self.message()

    # def lineReceived(self, line):
    #    print "line received - ", line
    #    self.message()
    #    self.transport.loseConnection()

    def dataReceived(self, data):
        print "Data Received : \n\n", data
        self.message()

    def message(self):
        command = raw_input("Enter the command: ")
        if str(command) == self.terminate:
            self.transport.loseConnection()
            return
        self.sendLine(str(command))


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
