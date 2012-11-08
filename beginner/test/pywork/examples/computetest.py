from com.pywork.examples import compute

__author__ = 'kannan'
import unittest

class TestCompute(unittest.TestCase):
    def test_sub_matrix(self):
        self.assertEqual(compute.subMatrix([[-2, 2, 3], [-1, 1, 3], [2, 0, -1]], 2), [[2, 3], [1, 3]])

if __name__ == '__main__':
    unittest.main()