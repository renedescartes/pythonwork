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

if __name__ == '__main__':
    unittest.main()