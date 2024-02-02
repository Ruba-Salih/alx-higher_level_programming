"""Define class TestMaxInt class"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):

    """Define unittests for max_integer([..])."""
    def setUp(self):
        self.li = [1, 2, 3, 5]

    def test_None(self):
        """Test a list of None."""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([None]), None)

    def test_one(self):
        """Test a list of one ele."""
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-8]), -8)

    def test_bool(self):
        """Test a list of boolen ele."""
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer([True, False, 100]), 100)
        self.assertEqual(max_integer([-23, False, -250]), False)

    def test_str(self):
        """Test a list of str ele."""
        self.assertEqual(max_integer('ruba'), 'u')
        self.assertEqual(max_integer(['ruba', 'salih', 'adam']), 'salih')
        self.assertEqual(max_integer('45982'), '9')
        self.assertEqual(max_integer(['a', 'n', 't', 's']), 't')
        self.assertEqual(max_integer(['a', 'x', '45']), 'x')

    def test_num(self):
        """Test a list of numbers ele."""
        self.assertEqual(max_integer([3, -4, 9.9, 0]), 9.9)
        self.assertEqual(max_integer([0.78, -0.100, 0.51]), 0.78)
        self.assertEqual(max_integer([1]), 1)



if __name__ == '__main__':
    unittest.main()
