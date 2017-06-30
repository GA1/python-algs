# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def solve(n):
    result = 0
    before = 1
    temp = 2
    if before < n and before % 2 == 0:
        result += before
    if temp < n and temp % 2 == 0:
        result += temp
    while temp < n:
        after = temp + before
        before = temp
        temp = after
        if temp % 2 == 0:
            result += temp
    return result


if __name__ == "__main__":
    print(solve(4000000))
