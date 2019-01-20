from src.datasctructures.queue import Queue


def get_valid_steps(steps, curr, a, n):
    result = []
    for i in range(len(steps)):
        s = steps[i]
        position = curr['position']
        if position + s == n or a[position + s] == 1:
            result.append(s)
    return result


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


def steps_lower_or_equal_than(n):
    steps = []
    i = 2
    while True:
        if i < 4:
            curr_fib = fibonacci(i)
        else:
            curr_fib = steps[i - 4] + steps[i - 3]
        if curr_fib <= n:
            steps.append(curr_fib)
        else:
            break
        i = i + 1
    return steps


def solution(a):
    n = len(a)
    q = Queue()
    q.enqueue({'position': -1, 'number_of_steps': 0})
    visited = [False for i in range(n + 1)]
    while not q.is_empty():
        curr = q.dequeue()
        curr_position = curr['position']
        curr_number_of_steps = curr['number_of_steps']
        if curr_position == n:
            return curr_number_of_steps
        steps = steps_lower_or_equal_than(n - curr_position)
        valid_steps = get_valid_steps(steps, curr, a, n)
        for s in valid_steps:
            if not visited[curr_position + s]:
                neighbor = {'position': curr_position + s, 'number_of_steps': curr_number_of_steps + 1}
                q.enqueue(neighbor)
                visited[curr_position + s] = True
    return -1
