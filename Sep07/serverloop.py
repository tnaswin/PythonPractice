from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor


class Echo(Protocol):

    delimiter = '\n'

    def dataReceived(self, data):
        print data
        d = data.split(",")
        name = d[0]
        age = d[1]
        stop = d[2]
        self.transport.write(" Name: " + str(name) + ",")
        self.transport.write(" Age: " + str(age) + ",")
        self.transport.write(stop)


def main():
    f = Factory()
    f.protocol = Echo
    reactor.listenTCP(8000, f)
    reactor.run()

if __name__ == '__main__':
    main()
