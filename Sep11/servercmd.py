import sys, socket
from subprocess import Popen, STDOUT, PIPE
import shlex

host = ''
port = 2004
buffer = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print "Socket successfully created"
s.bind((host, port))
print("Server started on port : %s"%port)
print("Now listening...\n")
s.listen(5)
conn, addr = s.accept()
print 'New connection from %s : %d' % (addr[0], addr[1])
while True:
    data = conn.recv(buffer)
    if not data:
        break
    elif data == 'end':
        conn.send('end')
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
