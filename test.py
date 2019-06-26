from twisted.internet import protocol
from twisted.internet import reactor
from twisted.protocols import basic


class MyClientProtocol( protocol.Protocol ):
    def sendData( self ):
            message = raw_input( 'Enter Message: ' )
            if message and ( message != "quit()" ):
                logging.debug( " ...Sending %s ...", message )
                self.transport.write( str( message ) )
            else:
                self.transport.loseConnection()

    def connectionMade( self ):
        print "Connection made to server!"

    def dataReceived( self, msg ):
        print msg
        self.sendData()

class MyClientFactory( protocol.ClientFactory ):
    protocol = MyClientProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()

reactor.connectTCP( "localhost", 1025, MyClientFactory() )
reactor.run()
