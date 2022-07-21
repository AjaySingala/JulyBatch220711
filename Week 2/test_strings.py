# Python code to demonstrate working of unittest
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        # initialize here.
        pass

    # Returns True if the string contains 4 a's.
    def test_strings_4as(self):
        self.assertEqual('a'*4, 'aaaa')

    # Returns True if the string is un upper case.
    def test_string_isupper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    # Returns TRUE if the string is in uppercase else returns False.
    def test_string_isupperorlower(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    # Returns true if the string is stripped and matches the given output.
    def test_strip(self):
        s = 'eyesforeyes'
        self.assertEqual(s.strip('eye'), 'sforeyes')
  
    # Returns true if the string splits and matches the given output.
    def test_split(self):        
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
  
if __name__ == '__main__':
    unittest.main()

