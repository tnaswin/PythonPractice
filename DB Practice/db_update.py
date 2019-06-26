import cgi
import txdbinterface as txdb
from twisted.web import server
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, defer

ac = 0
val = 0
balance = 0


class DbOperation():
    """Class to perform Database Operations.
    Get or update balace for the account.
    """

    def get_data(self):
        """Retrieve balance from the database."""
        self.query = "select bal from bank where account = %s" % ac
        print self.query
        self.df = txdb.execute(self.query)
        self.df.addCallback(self.on_db)
        self.df.addErrback(self.err_db)

    def on_db(self, result):
        print "result db"
        self.result = result[0]
        global balance
        balance = self.result['bal']
        print balance
        if not result:
            return err_db(None)

    def update_data(self):
        """Update the balance in database."""
        self.query = "update bank set bal = %s where account = %s" % (val, ac)
        print self.query
        self.df = txdb.execute(self.query)
        self.df.addCallback(self.new_data)
        self.df.addErrback(self.err_db)
        return self.df

    def new_data(self, result):
        print "new data"
        print result
        self.get_data()

    def err_db(self, error):
        print 'error db'
        print error

    def delayed_render(self, request):
        request.write('''<html><body>Current Balance is : %s
                         <form action="/form2" method="POST">
                         Update balance:<input name="val" type="text" required>
                         <button type="submit" value="Submit">Update</button>
                         </form></body></html>''' % balance)

    def delayed_render2(self, request):
        request.write('''<html><body>New Balance is : %s
                        <form action="/form2" method="POST">
                        Update balance:<input name="val" type="text" required>
                        <button type="submit" value="Submit">Update</button>
                        </form></body></html>''' % balance)
        request.finish()


class WebPage(Resource):
    """Form 1."""

    def render_GET(self, request):
        """Form to get the account number from the user."""
        return '''
                <html><body>
                <form action="/form1" method="POST">
                Enter your account number:<input name="ac" type="text" required>
                <button type="submit" value="Submit">Show balance</button>
                </form></body></html>
                '''

    def render_POST(self, request):
        global ac
        ac = cgi.escape(request.args["ac"][0])
        print "WebPage"
        print ac
        dbo = DbOperation()
        dbo.get_data()
        reactor.callLater(1, dbo.delayed_render, request)
        return server.NOT_DONE_YET


class NewPage(Resource):
    """Form 2."""

    def render_POST(self, request):
        global val
        val = cgi.escape(request.args["val"][0])
        dbo = DbOperation()
        dbo.update_data()
        reactor.callLater(1, dbo.delayed_render2, request)
        return server.NOT_DONE_YET


root = Resource()
root.putChild("form1", WebPage())
root.putChild("form2", NewPage())
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
