from twisted.protocols import basic
from twisted.internet import protocol, reactor

class HTTPEchoProtocol(basic.LineReceiver):


    def __init__(self):
        self.lines = []
    def lineReceived(self, line):
#        print "hello"
        self.lines.append(line)
        if not line:
            self.sendResponse()

    def sendResponse(self):
        self.sendLine(r"HTTP/1.1 200 OK")
        responseBody = "You said:\r\n\r\n" + "\r\n".join(self.lines)
        self.transport.write(responseBody)
        self.transport.loseConnection()


class HTTPEchoFactory(protocol.ServerFactory):


    def buildProtocol(self, addr):
        return HTTPEchoProtocol()


reactor.listenTCP(8000, HTTPEchoFactory())
reactor.run()
