import sys, socket
import threading
from thread import *
from subprocess import Popen, STDOUT, PIPE
import shlex

print_lock = threading.Lock()

def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            print('Exiting...')
            break
            """try:
                print_lock.release()
                break
            except Exception as e:
                c.send(str(e)+" , ERROR.\n")
        elif data == 'end':
            c.send(data)"""
        else:
            try:
                out = Popen(shlex.split(data), stdout=PIPE, stderr=PIPE)
                stdout, stderr = out.communicate()
                print "stdout - \n", stdout
                if not stdout:
                    c.send("Invalid Command.")
                c.send(stdout)
            except Exception as e:
                c.send(str(e)+" , Try again.\n")
    c.close()

def main():
    clients={}
    host = socket.gethostname()
    port = 2004
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print "Socket successfully created"
    s.bind((host, port))
    print("Server started on port : %s"%port)
    s.listen(5)
    print("Now listening...\n")
    while True:
        c, addr = s.accept()
        clients[addr] = c
        pressed = 0
        for eachsocket, eachaddrtuple in clients.iteritems():
            print 'Receiving data from :  %s' %eachaddrtuple
            start_new_thread(threaded, (c,))
    s.close()

if __name__ == '__main__':
    main()
