from subprocess import Popen, STDOUT, PIPE
from socket import socket
from time import sleep

server_sock = socket()
server_sock.bind(('', 8000))
server_sock.listen(4)

def close_process(p):
    p.stdin.close()
    p.stdout.close()

while 1:
    try:
        client, client_address = server_sock.accept()
        data = client.recv(8192)
    except:
        break
    # First, we open a handle to the external command to be run.
    process = Popen(data.decode('utf-8'), shell=True, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    # Wait for the command to finish
    # (.poll() will return the exit code, None if it's still running)
    while process.poll() == None:
        sleep(0.025)
    # Then we send whatever output the command gave us back via the socket
    # Python3: sockets never convert data from byte objects to strings,
    # so we'll have to do this "manually" in case you're confused from Py2.X
    try:
        client.send(bytes(process.stdout.read(), 'UTF-8'))
    except:
        pass

    # And finally, close the stdout/stdin of the process,
    # otherwise you'll end up with "to many filehandles openened" in your OS.
    close_process(process)
    client.close()

server_sock.close()
