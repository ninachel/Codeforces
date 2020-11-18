def max_dist(a):
    result = 0
    for i in range(len(a) - 1):
        current_dist = a[i + 1] - a[i]
        if current_dist > result:
            result = current_dist
    return result


n, length = map(int, input().split())
a = sorted(list(map(int, input().split())))
answer = max(max_dist(a) / 2, max(a[0] - 0, length - a[n - 1]))
print(answer)