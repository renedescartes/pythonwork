import unittest
from com.pywork.examples import problem104

class TestProblem104(unittest.TestCase):

    def setUp(self):
        pass

    def test_pandigital(self):
        self.assertTrue(problem104.is_pandigital(431259876))
        self.assertTrue(problem104.is_pandigital([4,3,1,2,5,9,8,7,6]))
        self.assertTrue(problem104.is_pandigital(map(str, [4,3,1,2,5,9,8,7,6])))
        self.assertFalse(problem104.is_pandigital(431239876))
        self.assertFalse(problem104.is_pandigital(4312876))
        self.assertFalse(problem104.is_pandigital(4312598769))

    def test_add_big_number(self):
        self.assertEquals(problem104.add_big_number([2, 3, 4, 5, 9, 1], [4, 2, 2]), [2, 3, 5, 0, 1, 3])
        self.assertEquals(problem104.add_big_number([3], [1]), [4])
        self.assertEquals(problem104.add_big_number([3], [9]), [1, 2])

    def test_answer(self):
        #self.assertEquals(problem104.answer(), 245)
        pass

if __name__ == '__main__':
    unittest.main()