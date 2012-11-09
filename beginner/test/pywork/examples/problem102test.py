from com.pywork.examples import problem102

import unittest

class TestProblem102(unittest.TestCase):

    def setUp(self):
        self.p1 = (-340, 495)
        self.p2 = (-153, -910)
        self.p3 = (835, -947)
        self.q1 = (-175, 41)
        self.q2 = (-421, -714)
        self.q3 = (574, -645)

    def test_area(self):
        self.assertEqual(problem102.area(self.p1, self.p2, self.p3), 690610.5)
        self.assertEqual(problem102.area((0, 3), (4, 0), (0, 0)), 6)

    def test_contains(self):
        self.assertTrue(problem102.contains_origin(self.p1, self.p2, self.p3))
        self.assertFalse(problem102.contains_origin(self.q1, self.q2, self.q3))

    def test_read(self):
        self.assertEquals(len(problem102.read_points("triangle.txt")), 1000)

    #def test_answer(self):
        #self.assertEquals(problem102.answer("triangle.txt"), 25)

if __name__ == '__main__':
    unittest.main()