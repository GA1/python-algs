from src.algs.fib_frog import steps_lower_or_equal_than, solution


def test_steps_lower_than_1():
    assert steps_lower_or_equal_than(1) == [1]


def test_steps_lower_than_2():
    assert steps_lower_or_equal_than(2) == [1, 2]


def test_steps_lower_than_13():
    assert steps_lower_or_equal_than(13) == [1, 2, 3, 5, 8, 13]


def test_solve_empty():
    assert solution([]) == 1


def test_solve_1():
    assert solution([1]) == 1


def test_solve_0_0_0_1_1_0_1_0_0_0_0():
    assert solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]) == 3
