import unittest

from ..src import *

class TestScript(unittest.TestCase):

    def test(self):
        assert "hello" == "hello"

if __name__ == '__main__':
    # ic.disable()
    unittest.main()
