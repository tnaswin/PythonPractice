from twisted.internet import reactor
import txdbinterface as txdb

def output(result):
    print(result)


def main():
    query = 'select account from bank'
    df = txdb.execute(query)
    df.addBoth(output)

if __name__ == "__main__":
    reactor.callLater(1, main)
    reactor.run()
