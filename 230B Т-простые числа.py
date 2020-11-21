# def sqrt(a):
#     """
#     square roots computation using binary search
#     :param a:
#     :return: square root of the param
#     """
#     left = 0
#     right = max(1, a)
#     EPS = 10**(-10)
#     while left < right - EPS:
#         mid = (left + right) / 2
#         if mid**2 > a:
#             right = mid
#         else:
#             left = mid
#     return left


def primes(a):
    """
    the sieve of Eratosthenes
    :param a:
    :return: all prime numbers on the interval [1, a]
    """
    primes = [True] * (a + 1)
    p = 2
    while p * p <= a:
        if primes[p]:
            for j in range(p * p, a + 1, p):
                primes[j] = False
        p += 1
    return primes


primes = primes(10**6)
n = int(input())
lst = list(map(int, input().split()))
for i in lst:
    if i == 1:
        print('NO')
    elif i**0.5 == int(i**0.5):
        if primes[(int(i**0.5))]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
