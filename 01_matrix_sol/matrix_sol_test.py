""" leetcode: https://leetcode.com/problems/01-matrix/"""

import unittest
from matrix_sol_1 import update_matrix_1
from matrix_sol_2 import update_matrix_2

class TestSolOne(unittest.TestCase):
    """
    Unit testing for solution 1.
    """
    def test_matrix_1(self):
        """
        Simple test.
        """
        test_mat = [[0], [1]]
        output_mat = update_matrix_1(test_mat)
        self.assertEqual([[0], [1]], output_mat)

    def test_matrix_2 (self):
        """
        Simple test.
        """
        test_mat = [[0,0,0],[0,1,0],[0,0,0]]
        output_mat = update_matrix_1(test_mat)
        self.assertEqual([[0,0,0],[0,1,0],[0,0,0]], output_mat)

    def test_matrix_3 (self):
        """
        Simple test.
        """
        test_mat = [[0,0,0],[0,1,0],[1,1,1]]
        output_mat = update_matrix_1(test_mat)
        self.assertEqual([[0,0,0],[0,1,0],[1,2,1]], output_mat)

class TestSolTwo(unittest.TestCase):
    """
    Unit testing for solution 1.
    """
    def test_matrix_1(self):
        """
        Simple test.
        """
        test_mat = [[0], [1]]
        output_mat = update_matrix_2(test_mat)
        self.assertEqual([[0], [1]], output_mat)

    def test_matrix_2 (self):
        """
        Simple test.
        """
        test_mat = [[0,0,0],[0,1,0],[0,0,0]]
        output_mat = update_matrix_2(test_mat)
        self.assertEqual([[0,0,0],[0,1,0],[0,0,0]], output_mat)

    def test_matrix_3 (self):
        """
        Simple test.
        """
        test_mat = [[0,0,0],[0,1,0],[1,1,1]]
        output_mat = update_matrix_2(test_mat)
        self.assertEqual([[0,0,0],[0,1,0],[1,2,1]], output_mat)

if __name__ == '__main__':
    unittest.main()

#End of matrix_sol_test.py file
