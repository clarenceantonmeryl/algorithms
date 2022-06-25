import math


def factorial(n: int):
    factorial = n
    k = n
    for i in range(0, k - 1):
        factorial *= (n - 1)
        n -= 1
    return math.log(factorial)


def factorial2(n: int):
    ln = 0
    for i in range(1, n+1):
        ln += math.log(i)
    return ln


print(factorial(6))
print(factorial2(6))
