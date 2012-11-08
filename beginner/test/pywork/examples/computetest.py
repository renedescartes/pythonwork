from com.pywork.examples import compute

__author__ = 'kannan'
import unittest

class TestCompute(unittest.TestCase):

    def setUp(self):
        self.matrix = [[-2, 2, 3], [-1, 1, 3], [2, 0, -1]]

    def test_sub_matrix(self):
        self.assertEqual(compute.subMatrix(self.matrix, 2), [[2, 3], [1, 3]])

    def test_determinant(self):
        self.assertEqual(compute.determinant(self.matrix), 6)

if __name__ == '__main__':
    unittest.main()