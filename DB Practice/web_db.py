import cgi

import txdbinterface as txdb

from twisted.web import server
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, defer


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
        self.get_data(ac)
        reactor.callLater(1, self._delayed_render, request)
        return server.NOT_DONE_YET

    def _delayed_render(self, request):
        request.write('<html><body>Current Balance is : %s</body></html>'
                        % self.balance)
        request.finish()

    def get_data(self, ac):
        self.query = "select bal from bank where account = %s" % ac
        print self.query
        self.df = txdb.execute(self.query)
        self.df.addCallback(self.on_db)
        self.df.addErrback(self.err_db)
        return self.df

    def on_db(self, result):
        print "result db"
        self.result = result[0]
        self.balance = self.result['bal']
        print self.balance
        if not result:
            return err_db(None)

    def err_db(self, error):
        print 'error db'
        print error


root = Resource()
root.putChild("form", WebPage())
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
