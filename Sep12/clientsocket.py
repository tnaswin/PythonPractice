import socket

def Main():
    host = ''
    port = 2004

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        cmd = raw_input("Enter command/ Enter end: ")
        s.send(cmd)
        data = s.recv(1024)
        msglen = len(data)
        print "got: %s" % data
        print "received: %d" % msglen
        ans = raw_input("\nDo you want to continue(y/n) :")
        if ans == 'y':
            continue
        else:
            print "Connection closed\n"
            break
    s.close()

if __name__ == '__main__':
    Main()
