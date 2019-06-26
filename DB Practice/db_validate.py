import cgi

import txdbinterface as txdb

from twisted.web import server
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, defer


account_num = 0
new_balance = 0
balance = 0
temp = 0


class DbOperation():
    """Class to perform Database Operations.
    Verify account number.
    Get or update balace for the account.
    """

    def on_verify(self):
        """Check if the account number exist in the database."""
        self.query = "select account from bank where account = %s" \
                    % account_num
        self.df = txdb.execute(self.query)
        self.df.addCallback(self.on_check)
        self.df.addErrback(self.err_db)
        return self.df

    def on_check(self,result):
        print "Verify account"
        print result
        print len(result)
        if result:
            global temp
            temp = 1
            print "check"
            return True
        else:
            return False

    def get_data(self):
        """Retrieve balance from the database."""
        self.query = "select bal from bank where account = %s" % account_num
        print self.query
        self.df = txdb.execute(self.query)
        self.df.addCallback(self.on_db)
        self.df.addErrback(self.err_db)
        return self.df

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
        self.query = "update bank set bal = %s where account = %s" \
                        % (new_balance, account_num)
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
        """
        Show balance to user and get new balance to be updated.
        """
        request.write('''
                      <html><body>Current Balance is : %s
                      <form action="/form2" method="POST">
                      Update balance:<input name="val" type="text" required>
                      <button type="submit" value="Submit">Update</button>
                      </form></body></html>
                      ''' % balance)

    def delayed_render2(self, request):
        """
        Show balance to user and get new balance to be updated
        """
        request.write('''
                      <html><body>New Balance is : %s
                      <form action="/form2" method="POST">
                      Update balance:<input name="val" type="text" required>
                      <button type="submit" value="Submit">Update</button>
                      </form></body></html>
                      ''' % balance)
        request.finish()


class WebPage(Resource):
    """Form 1."""

    def render_GET(self, request):
        """Form to get the account number from the user."""
        return '''
               <html><body>
               <form action="/form1" method="POST">
               Enter account number:<input name="ac" type="text" required>
               <button type="submit" value="Submit">Show balance</button>
               </form></body></html>
               '''

    def render_POST(self, request):
        global account_num, temp
        account_num = cgi.escape(request.args["ac"][0])
        temp = 0
        print "WebPage"
        print account_num
        self.dbo = DbOperation()
        self.dbo.on_verify()
        reactor.callLater(1, self._delayed_render, request)
        return server.NOT_DONE_YET

    def _delayed_render(self, request):
        if not temp:
            request.write(
                '''
                <html><body>
                "Invalid Account number"
                <form action="/form1" method="POST">
                Enter account number:<input name="ac" type="text" required>
                <button type="submit" value="Submit">Show balance</button>
                </form></body></html>
                '''
                )
        else:
            self.dbo.get_data()
            reactor.callLater(1, self.dbo.delayed_render, request)
            return server.NOT_DONE_YET


class NewPage(Resource):
    """Form 2."""

    def render_POST(self, request):
        global new_balance
        new_balance = cgi.escape(request.args["val"][0])
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
