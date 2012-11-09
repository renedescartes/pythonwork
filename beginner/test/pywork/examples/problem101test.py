from com.pywork.examples import problem101

__author__ = 'kannan'
import unittest

class TestCompute(unittest.TestCase):

    def setUp(self):
        self.matrix = [[-2, 2, 3], [-1, 1, 3], [2, 0, -1]]

    def test_sub_matrix(self):
        self.assertEqual(problem101.sub_matrix(self.matrix, 2), [[2, 3], [1, 3]])

    def test_determinant(self):
        self.assertEqual(problem101.determinant(self.matrix), 6)

    def test_evaluate(self):
        p = (6, -11, 6)
        self.assertEqual(problem101.evaluate(p, 3), 27)
        self.assertEqual(problem101.evaluate_terms(p, 4), [1, 8, 27, 58])

    def test_vandermonde(self):
        self.assertEqual(problem101.vander_monde_matrix(3), [[1, 1, 1], [4, 2, 1], [9, 3, 1]])

    def test_replace_column(self):
        self.assertEqual(problem101.replace_column(self.matrix, [7, 8, 3], 2), [[-2, 2, 7], [-1, 1, 8], [2, 0, 3]])

    def test_solve_vandermonde(self):
        matrix = problem101.vander_monde_matrix(3)
        self.assertEqual(problem101.cramers_solution(matrix, [1, 8, 27]), [6, -11, 6])

    def test_fit(self):
        self.assertEqual(problem101.first_incorrect_term([6, -11, 6], [1, 8, 27, 64, 125]), 58)

    def test_sum_of_bop(self):
        self.assertEqual(problem101.sum_of_bop([1, 0, 0, 0]), 74)
        #The below will take 2 minutes to complete
        #self.assertEqual(problem101.sum_of_bop([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]), 37076114526)


if __name__ == '__main__':
    unittest.main()