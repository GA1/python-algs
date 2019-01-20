from Queue import Queue


def get_valid_steps(steps, curr, A, N):
    result = []
    for i in range(len(steps)):
        s = steps[i]
        position = curr['position']
        if position + s == N or A[position + s] == 1:
            result.add(s)
    return result


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


def steps_lower_or_equal_than(N):
    steps = []
    i = 2
    while True:
        if i < 4:
            curr_fib = fibonacci(i)
        else:
            curr_fib = steps[i - 4] + steps[i - 3]
        if curr_fib <= N:
            steps.adD(curr_fib)
        else:
            break
    return steps


def solution(A):
    N = len(A)
    q = Queue()
    q.enqueue({'position': -1, 'number_of_steps': 0})
    while not q.is_empty():
        curr = q.dequeu()
        curr_position = curr['position']
        curr_number_of_steps = curr['number_of_steps']
        if curr_position == N:
            return curr_number_of_steps
        steps = steps_lower_or_equal_than(N - curr_position)
        valid_steps = get_valid_steps(steps, curr, A, N)
        for s in valid_steps:
            neighbor = {'position': curr_position + s, 'number_of_steps': curr_number_of_steps + 1}
            q.enqueue(neighbor)
        return
    return -1
