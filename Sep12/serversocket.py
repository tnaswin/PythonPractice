import sys, socket
import threading
from thread import *
from subprocess import Popen, STDOUT, PIPE
import shlex

print_lock = threading.Lock()

def threaded(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            print('Exiting...')
            print_lock.release()
            break
        elif data == 'end':
            conn.send(data)
        else:
            try:
                out = Popen(shlex.split(data), stdout=PIPE, stderr=PIPE)
                #print "out - ", out
                stdout, stderr = out.communicate()
                print "stdout - \n", stdout
                if not stdout:
                    conn.send("Success")
                conn.send(stdout)
            except Exception as e:
                conn.send(str(e)+" , Try again.\n")
    conn.close()

def Main():
    host = ''
    port = 2004
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print "Socket successfully created"
    s.bind((host, port))
    print("Server started on port : %s"%port)
    s.listen(5)
    print("Now listening...\n")
    while True:
        conn, addr = s.accept()
        print_lock.acquire()
        print 'New connection from %s : %d' % (addr[0], addr[1])
        start_new_thread(threaded, (conn,))
    s.close()

if __name__ == '__main__':
    Main()
