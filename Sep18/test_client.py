import unittest
from clientsoc import ClientProgram


class ClientTest(unittest.TestCase):
    """Tests for `clientsoc.py`."""

    def test_connect(self):
        print "Connect"
        c = ClientProgram()
        c.read_data()
        print "End"


if __name__ == '__main__':
    unittest.main()
