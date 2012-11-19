from com.pywork.examples import problem105

import unittest

class TestProblem105(unittest.TestCase):

    def setUp(self):
        pass

    def test_area(self):
        self.assertEqual(problem105.answer("sets.txt"), 73702)

if __name__ == '__main__':
    unittest.main()