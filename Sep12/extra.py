import socket

def Main():
    host = ''
    port = 2004

    s2= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect((host, port))

    while True:
        cmd2 = raw_input("Enter command/ Enter end: ")
        s2.send(cmd2)
        data2 = s2.recv(1024)
        msglen2 = len(data2)
        print "got: %s" % data2
        print "received: %d" % msglen2
        ans = raw_input("\nDo you want to continue(y/n) :")
        if ans == 'y':
            continue
        else:
            print "Connection closed\n"
            break
    s.close()

if __name__ == '__main__':
    Main()
