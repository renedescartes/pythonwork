from com.pywork.examples import compute

__author__ = 'kannan'
import unittest

class TestCompute(unittest.TestCase):

    def test_sub_matrix(self):
        matrix = [[-2, 2, 3], [-1, 1, 3], [2, 0, -1]]
        self.assertEqual(compute.subMatrix(matrix, 2), [[2, 3], [1, 3]])

    def test_determinant(self):
        self.assertEqual(compute.determinant([[-2, 2, 3], [-1, 1, 3], [2, 0, -1]]), 6)

if __name__ == '__main__':
    unittest.main()