import sys
import select
import socket
import unittest
from serversoc import ServerProgram


class ServerTest(unittest.TestCase):
    """Tests for `serversoc.py`."""

    def test_connect(self):
        print "Connect"
        p = ServerProgram()
        p.main()
        print "End"


if __name__ == '__main__':
    unittest.main()
