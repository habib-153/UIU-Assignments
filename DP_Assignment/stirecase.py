def count(n, max_act, k):
    if n == 0:
        if k >= 2:
            return 1
        return 0
    if n < 0 or max_act <= 0:
        return 0
    if memo[n][max_act][k] != -1:
        return memo[n][max_act][k]
    
    result = count(n, max_act -1, k)
    new_k = min(k+1, 2)
    result += count(n - max_act, max_act -1, new_k)
    memo[n][max_act][k] = result

    return result

n = int(input())
memo = [[[-1 for _ in range(3)] for _ in range(n+1)] for _ in range(n+1)]

print(count(n, n, 0))