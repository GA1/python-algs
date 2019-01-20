from src.pe.pe_0002 import solve


def test_001():
    assert 0 == solve(1)
    assert 0 == solve(2)
    assert 2 == solve(3)
    assert 2 == solve(4)
    assert 2 == solve(8)


def test_002():
    assert 10 == solve(9)
