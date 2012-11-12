import unittest
from com.pywork.examples import problem103

class TestProblem102(unittest.TestCase):

    def setUp(self):
        pass

    def test_rule1(self):
        self.assertTrue(problem103.is_rule1_satisfied([3, 5, 6, 7]))
        self.assertFalse(problem103.is_rule1_satisfied([5, 6, 7, 11]))

    def test_rule2(self):
        self.assertTrue(problem103.is_rule2_satisfied([6, 9, 11, 12, 13]))
        self.assertFalse(problem103.is_rule2_satisfied([3, 9, 11, 12, 13]))

    def test_compute_optimal(self):
        self.assertEquals(problem103.computed_optimal_set(1), [1])
        self.assertEquals(problem103.computed_optimal_set(2), [1,2])
        self.assertEquals(problem103.computed_optimal_set(3), [2, 3, 4])
        self.assertEquals(problem103.computed_optimal_set(4), [3, 5, 6, 7])
        self.assertEquals(problem103.computed_optimal_set(5), [6, 9, 11, 12, 13])
        self.assertEquals(problem103.computed_optimal_set(6), [11, 17, 20, 22, 23, 24])

    def test_iterator(self):
        iterator = problem103.adjustment_vector_iterator(7, 3)
        self.assertEquals(len(list(iterator)), 1716)

if __name__ == '__main__':
    unittest.main()