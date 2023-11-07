""" leetcode: https://leetcode.com/problems/seat-reservation-manager """

import unittest
from seat_sol_1 import binary_insert

class TestSolOne(unittest.TestCase):
    """
    Unit testing for solution 1.
    """
    def test_begin (self):
        """
        Simple test.
        """
        my_list = [2,3,4,5]
        num = 1
        binary_insert(my_list, num)
        self.assertEqual(my_list, [1,2,3,4,5])

    def test_end (self):
        """
        Simple test.
        """
        my_list = [1,2,3,4]
        num = 5
        binary_insert(my_list, num)
        self.assertEqual(my_list, [1,2,3,4,5])
        
    def test_1(self):
        """
        Simple test.
        """
        my_list = [1,2,3,4,6,7]
        num = 5
        binary_insert(my_list, num)
        self.assertEqual(my_list, [1,2,3,4,5,6,7])

    def test_2 (self):
        """
        Simple test.
        """
        my_list = [1,2,3,4,6]
        num = 5
        binary_insert(my_list, num)
        self.assertEqual(my_list, [1,2,3,4,5,6])

    def test_3 (self):
        """
        Simple test.
        """
        my_list = [1,3,4,5]
        num = 2
        binary_insert(my_list, num)
        self.assertEqual(my_list, [1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()

#End of matrix_sol_test.py file
