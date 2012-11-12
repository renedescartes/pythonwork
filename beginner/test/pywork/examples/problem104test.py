import unittest
from com.pywork.examples import problem104

class TestProblem104(unittest.TestCase):

    def setUp(self):
        pass

    def test_pandigital(self):
        self.assertTrue(problem104.is_pandigital(431259876))
        self.assertFalse(problem104.is_pandigital(431239876))
        self.assertFalse(problem104.is_pandigital(4312876))
        self.assertFalse(problem104.is_pandigital(4312598769))

if __name__ == '__main__':
    unittest.main()