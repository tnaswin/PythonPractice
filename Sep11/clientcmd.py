import sys, socket

host = ''
port = 2004
buffer = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    cmd = raw_input('Enter a command: ')
    s.send(cmd)
    data = s.recv(buffer)
    msglen = len(data)
    print "got: %s" % data
    print "received: %d" % msglen
    if data == 'end':
        print 'exiting...'
        sys.exit(0)
