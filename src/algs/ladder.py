
def solution(a, b):
    result = []
    for i in range(len(a)):
        result.append(ladder_with_modulo(a[i], 2**b[i]))
    return result


def ladder_with_modulo(n, q):
    fibs = [1, 2]
    if n == 1:
        return 1
    elif n == 2:
        return 2 % q
    else:
        for i in range(2, n):
            fibs.append((fibs[i - 2] + fibs[i - 1]) % q)
        return fibs[len(fibs) - 1]


def ladder(N):
    prevprev = 1
    prev = 2
    if N == 1:
        return prevprev
    elif N == 2:
        return prev
    else:
        for i in range(3, N + 1):
            result = prevprev + prev
            prevprev = prev
            prev = result
        return result
