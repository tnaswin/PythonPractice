import socket


class ClientProgram():


    def connect(self):
        self.host = socket.gethostname()
        self.port = 2004
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))

    def read_data(self):
        self.connect()
        while True:
            self.cmd = raw_input("Enter command: ")
            self.s.send(self.cmd)
            self.data = self.s.recv(1024)
            self.msglen = len(self.data)
            print "got: %s" % self.data
            print "received: %d" % self.msglen
            if self.data == "end":
                print "Connection closed\n"
                break
            self.ans = raw_input("\nDo you want to continue(y/n) :")
            if self.ans == 'y':
                continue
            else:
                self.s.send(self.ans)
                print "Connection closed\n"
                break
        self.s.close()


if __name__ == '__main__':
    c = ClientProgram()
    c.read_data()
