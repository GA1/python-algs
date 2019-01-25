from src.algs.ladder import ladder, ladder_with_modulo, solution


def test_1():
    assert ladder(1) == 1


def test_2():
    assert ladder(2) == 2


def test_3():
    assert ladder(3) == 3


def test_4():
    assert ladder(4) == 5


def test_5():
    assert ladder(5) == 8


def test_ladder_modulo_1_1():
    assert ladder_with_modulo(1, 1) == 1


def test_ladder_modulo_3_2():
    assert ladder_with_modulo(3, 2) == 1


def test_ladder_modulo_5_2():
    assert ladder_with_modulo(5, 2) == 0
    assert ladder(5) % 2 == 0


def test_ladder_modulo_5_4():
    assert ladder_with_modulo(5, 4) == 0
    assert ladder(5) % 4 == 0


def test_ladder_modulo_7_3():
    assert ladder_with_modulo(7, 3) == 0
    assert ladder(7) % 3 == 0


def test_ladder_modulo_7_3():
    assert ladder_with_modulo(7, 5) == 1
    assert ladder(7) % 5 == 1


def test_ladder_modulo_2_2():
    assert ladder_with_modulo(2, 2) == 0
    assert ladder(2) % 2 == 0


def test_solve_example():
    assert solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]) == [5, 1, 8, 0, 1]
