import unittest
from src.pe.pe_0002 import solve


class MyTest(unittest.TestCase):

    def test_001(self):
        self.assertEqual(0, solve(1))
        self.assertEqual(0, solve(2))
        self.assertEqual(2, solve(3))
        self.assertEqual(2, solve(4))






