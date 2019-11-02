"""THis is our testing file for square root functions"""

import unittest # built in so we don't need a pip install

from sqrt import newton_sqrt, lazy_sqrt, builtin_sqrt

#Our class for square root functions.
class SqrtTests(unittest.TestCase):
    """These are our tests for square root functions"""
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)   #checking to see if lazy_sqrt(9) == 3

    def test_sqrt2(self):
        self.assertAlmostEqual(round(newton_sqrt(2), 3), 1.414)

class OtherTests(unittest.TestCase):
    def test_thing(self):
        pass

if __name__== '__main__':
    unittest.main()
