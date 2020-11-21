n, k = map(int, input().split())
programming_time = 240 - k
problems = 0
while programming_time > 0:
    if problems == n:
        break
    elif programming_time - 5 * (problems + 1) >= 0:
        problems += 1
        programming_time -= 5 * problems
    else:
        break
print(problems)
