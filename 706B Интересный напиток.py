from bisect import bisect_right


n = int(input())
prices = sorted(list(map(int, input().split())))
days = int(input())
money = []
for _ in range(days):
    day_budget = int(input())
    money.append(day_budget)
for i in range(days):
    budget = money[i]
    result = bisect_right(prices, budget)
    print(result)
