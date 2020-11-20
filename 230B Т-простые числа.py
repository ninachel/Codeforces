def is_prime(a):
    d = 2
    while d**2 <= a and a % d != 0:
        d += 1
    return d**2 > a


def sqrt(a):
    """
    square roots computation using binary search
    :param a:
    :return: square root of the param
    """
    left = 0
    right = max(1, a)
    EPS = 10**(-6)
    while left < right - EPS:
        mid = (left + right) / 2
        if mid**2 > a:
            right = mid
        else:
            left = mid
    return round(left)


def is_t_simple(a):
    return 4 <= a == sqrt(a)**2 and is_prime(sqrt(a))


n = int(input())
lst = list(map(int, input().split()))
for i in range(n):
    if is_t_simple(lst[i]):
        print('YES')
    else:
        print('NO')
