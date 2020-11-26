n = int(input())
a = list(map(int, input().split()))
f = [1] * n
f[0] = 1
for i in range(1, n):
    if a[i] >= a[i - 1]:
        f[i] += f[i - 1]
print(max(f))
