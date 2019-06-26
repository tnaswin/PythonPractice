import select
import socket
import sys
from subprocess import Popen, STDOUT, PIPE
import shlex

def main():
    host = socket.gethostname()
    port = 2004
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)
    server.bind((host,port))
    server.listen(5)
    input = [server,]
    running = 1
    
    while running:
      readable,writeable,exceptional = select.select(input,[],[])

      for s in readable:

        if s == server:
          client, address = server.accept()
          input.append(client)
          print 'New client added : %s'%str(address)

        else:
          data = s.recv(1024)
          if data:
              try:
                  out = Popen(shlex.split(data), stdout=PIPE, stderr=PIPE)
                  stdout, stderr = out.communicate()
                  print "stdout - \n", stdout
                  if not stdout:
                      s.send("Invalid Command.")
                  s.send(stdout)
              except Exception as e:
                  s.send(str(e)+" , Try again.\n")
          else:
              s.close()
              input.remove(s)

    server.close()

if __name__ == '__main__':
    main()
