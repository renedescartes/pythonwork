import unittest
from com.pywork.examples import problem103

class TestProblem102(unittest.TestCase):

    def setUp(self):
        pass

    def test_area(self):
        self.assertTrue(problem103.is_rule1_satisfied([3, 5, 6, 7]))
        self.assertFalse(problem103.is_rule1_satisfied([5, 6, 7, 11]))

if __name__ == '__main__':
    unittest.main()