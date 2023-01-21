import sys
import unittest
sys.path.append('..')
print(sys.path)
from python import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(1, 2)
        print(result)
        self.assertEqual(result, 3)


unittest.main()