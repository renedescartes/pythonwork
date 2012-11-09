from com.pywork.examples import problem102

import unittest

class TestProblem102(unittest.TestCase):

    def setUp(self):
        self.p1 = (-340, 495)
        self.p2 = (-153, -910)
        self.p3 = (835, -947)

    def test_area(self):
        self.assertEqual(problem102.area(self.p1, self.p2, self.p3), 690610)
        self.assertEqual(problem102.area((0, 3), (4, 0), (0, 0)), 6)

if __name__ == '__main__':
    unittest.main()