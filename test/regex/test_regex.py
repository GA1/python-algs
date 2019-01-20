import re


def test_replace_one_letter_01():
    assert re.sub('a', 'b', 'ab') == 'bb'


def test_replace_02():
    assert re.sub('a', 'b', 'aa') == 'bb'


def test_replace_03():
    assert re.sub('ab', 'c', 'babab') == 'bcc'


def test_replace_04():
    assert re.sub('ab', 'c', 'babab') == 'bcc'


def test_replace_05():
    assert re.sub(',', ', ', 'You,and Me.') == 'You, and Me.'


def test_replace_06():
    assert re.sub(',(?!\s)', ', ', 'You,me, him') == 'You, me, him'


def test_replace_07():
    assert re.sub('\.(?=\S)', '. ', 'You.You.') == 'You. You.'


def test_replace_08():
    assert re.sub('.', 'A', '..') == 'AA'
    assert re.sub('!', 'A', '!!') == 'AA'
    assert re.sub('\?', 'A', '??') == 'AA'
    assert re.sub('[.!\?]', 'A', '!.?') == 'AAA'


def test_split_01():
    s = """You!Are you Tom? I am Danny."""
    assert re.findall('.*?[.!\?]', s) == ['You!', 'Are you Tom?', ' I am Danny.']
