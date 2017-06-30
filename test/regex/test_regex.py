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
        self.assertEqual(re.sub(',', ', ', 'You,and Me.'), 'You, and Me.')

    def test_replace_06(self):
        self.assertEqual(re.sub(',(?!\s)', ', ', 'You,me, him'), 'You, me, him')

    def test_replace_07(self):
        self.assertEqual(re.sub('\.(?=\S)', '. ', 'You.You.'), 'You. You.')

    def test_replace_08(self):
        self.assertEqual(re.sub('.', 'A', '..'), 'AA')
        self.assertEqual(re.sub('!', 'A', '!!'), 'AA')
        self.assertEqual(re.sub('\?', 'A', '??'), 'AA')
        self.assertEqual(re.sub('[.!\?]', 'A', '!.?'), 'AAA')

    def test_split_01(self):
        s = """You!Are you Tom? I am Danny."""
        self.assertEqual(['You!', 'Are you Tom?', ' I am Danny.'], re.findall('.*?[.!\?]', s))
        



