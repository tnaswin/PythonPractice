#import subprocess
from subprocess import Popen, PIPE
import shlex
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor


class Echo(Protocol):

    def dataReceived(self, data):
        print "Command is:", data
        #output = subprocess.check_output("ls | grep f89e7000 | awk '{print $2}'", shell=True)
        #out = str(subprocess.call(shlex.split(data)))
        #output = out.decode("utf-8")
        #proc = subprocess.Popen([data], stdout=subprocess.PIPE)
        #        (out, err) = proc.communicate()
        #out = subprocess.check_output(data)
        #print "program output:", stdout
        # self.transport.write(out)
        #a = "ls"
        #print "a: ", a
        #print "data: ", data
        try:
            out = Popen(shlex.split(data), stdout=PIPE, stderr=PIPE)
            print "out - ", out
            stdout, stderr = out.communicate()
            print "stdout - \n", stdout
            if not stdout:
                return self.transport.write("Success")
            self.transport.write(stdout)
        except Exception as e:
            return self.transport.write(str(e)+" , Try again.\n")


def main():
    f = Factory()
    f.protocol = Echo
    reactor.listenTCP(8000, f)
    reactor.run()


if __name__ == '__main__':
    main()
