import unittest
import re

class MyTest(unittest.TestCase):
    def test_replace_one_letter_01(self):
        self.assertEqual(re.sub('a', 'b', 'ab'), 'bb')

    def test_replace_02(self):
        self.assertEqual(re.sub('a', 'b', 'aa'), 'bb')

    def test_replace_03(self):
        self.assertEqual(re.sub('ab', 'c', 'babab'), 'bcc')

    def test_replace_04(self):
        self.assertEqual(re.sub('ab', 'c', 'babab'), 'bcc')

    def test_replace_05(self):
        self.assertEqual(re.sub('ab', 'c', 'babab'), 'bcc')