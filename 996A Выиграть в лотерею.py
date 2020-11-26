n = int(input())
values = [100, 20, 10, 5, 1]
result = 0
money_left = n
while money_left > 0:
    for value in values:
        money_left = n % value
        banknotes = n // value
        result += banknotes
        n = money_left
print(result)
