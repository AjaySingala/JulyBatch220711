"""
Assuming this is file called test.py, then this string is
first statement in the file. This will become the "test" module's
docstring when the file is imported.
"""
class TestClass(object):
    """The test class's docstring"""

    def test_method(self):
        """The test method's docstring"""

def test_function():
    """The test function's docstring"""

import test
help(test)
help(test.TestClass)
help(test.TestClass.test_method)
help(test.test_function)
