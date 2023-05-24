from .dyn_import import dyn_import
dyn_import()


import unittest

class TestScript(unittest.TestCase):

    def setUp(self):
        dyn_import()



if __name__ == '__main__':
    # ic.disable()
    unittest.main()
