import sys
import select
import socket
import shlex
from subprocess import Popen, STDOUT, PIPE


class ServerProgram():


    def __init__(self):
        self.running = 1

    def connect(self):
        self.host = socket.gethostname()
        self.port = 2004
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.setblocking(0)
        self.server.bind((self.host,self.port))
        self.server.listen(5)

    def disconnect(self):
        self.running = 0

    def main(self):
        self.connect()
        self.input = [self.server,]
        while self.running:
            self.readable, self.writeable, self.exceptional = select.select(self.input, [], [])
            for self.s in self.readable:
                if self.s == self.server:
                    self.client, self.address = self.server.accept()
                    self.input.append(self.client)
                    print 'New client added : %s'%str(self.address)
                else:
                    self.data = self.s.recv(1024)
                    if self.data == 'end' or self.data == 'n':
                        self.s.send(self.data)
                        self.disconnect()
                    elif self.data:
                        try:
                            self.out = Popen(shlex.split(self.data), stdout=PIPE, stderr=PIPE)
                            stdout, stderr = self.out.communicate()
                            print "stdout - \n", stdout
                            if not stdout:
                                self.s.send("Invalid Command.")
                            self.s.send(stdout)
                        except Exception as self.e:
                            s.send(str(self.e)+" , Try again.\n")
                    else:
                        self.s.close()
                        self.input.remove(self.s)
        self.server.close()


if __name__ == '__main__':
    p = ServerProgram()
    p.main()
