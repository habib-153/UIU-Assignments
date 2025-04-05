money = None
count = None
max_amount = 30
max_money = 110
prices = []
memo = []

def solve(gold, budget):
    if budget < 0:
        return float('-inf')
    if gold == count:
        return money - budget
    if memo[gold][budget] != -1:
        return memo[gold][budget]
    max_spent = -10000
    for item_price in prices[gold]:
        max_spent = max(max_spent, solve(gold+1, budget-item_price))
    memo[gold][budget] = max_spent
    return max_spent

n = int(input())
for _ in range(n):
    line = list(map(int, input().split()))
    money = line[0]
    count = line[1]
    prices = []
    memo = [[-1 for _ in range(max_money)] for _ in range(max_amount)]

    for i in range(count):
        garment_prices = list(map(int, input().split()))
        prices.append(garment_prices[1:])

    result = solve(0, money)
    if result < 0:
        print('no solution')
    else:
        print(result)





# ############## V2 ################################
# m = None
# c = None
# max_amt = 30
# max_m = 110
# price = [[]]
# memo = [[]]


# def fg(g, b):
#     if b < 0:
#         return -float('inf')
#     if g == c:
#         return m-b

#     if memo[g][b] != -1:
#         return memo[g][b]

#     bspent = -10000
#     for modelp in price[g]:
#         bspent = max(bspent, fg(g+1, b-modelp))
#     memo[g][b] = bspent
#     return bspent


# n = int(input())
# for i in range(n):
#     line = list(map(int, input().split()))
#     m = line[0]
#     c = line[1]
#     price = []
#     memo = [[-1 for i in range(max_m)] for j in range(max_amt)]

#     for i in range(c):
#         pgarment = list(map(int, input().split()))
#         price.append(pgarment[1:])

#     result = fg(0, m)
#     if result < 0:
#         print('no solution')
#     else:
#         print(result)
