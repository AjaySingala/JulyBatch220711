import unittest

class SimpleTest(unittest.TestCase):
    # returns true or false.
    def test(self):
        i = 10
        j = 8
        if(i == 0 or j == 0):
            self.assertFalse(True)

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
