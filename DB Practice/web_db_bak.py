import cgi
import txdbinterface as txdb
from twisted.web import server
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, defer


class GetDb():

    def getData(self, ac):
        self.query = "select bal from bank where account = %s" % ac
        print self.query
        self.df = txdb.execute(self.query)
        self.df.addCallback(self.onDb)
        self.df.addErrback(self.errDb)

    def onDb(self, result):
        print "result db"
        self.result = result[0]
        self.balance = self.result['bal']
        print self.balance
        if not result:
            return errDb(None)

    def errDb(self, error):
        print 'error db'
        print error


class WebPage(Resource):
    def render_GET(self, request):
        return '''
                <html><body>
                <form method="POST">
                Enter your account number: <input name="ac" type="text" />
                <button type="submit" value="Submit">Show balance</button>
                </form>
                </body></html>'''

    def render_POST(self, request):
        ac = cgi.escape(request.args["ac"][0])
        bank = GetDb()
        bank.getData(ac)
        reactor.callLater(1, self._delayedRender, request)
        return server.NOT_DONE_YET

    def _delayedRender(self, request):
        request.write('<html><body>Current Balance is : %s</body></html>'
                      % GetDb.self.balance)
        request.finish()


root = Resource()
root.putChild("form", WebPage())
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
