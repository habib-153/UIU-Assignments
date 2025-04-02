t = int(input())
for case in range(1, t+1):
    n = int(input())
    r = 2*n-1
    memo = []
    for _ in range(r):
        memo.append([int(x) for x in input().split()])

    # Upper triangle
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                memo[i][j] += memo[i-1][j]
            elif i == j:
                memo[i][j] += memo[i-1][j-1]
            else:
                memo[i][j] += max(memo[i-1][j-1], memo[i-1][j])

    # Lower triangle
    for i in range(n, r):
        for j in range(r-i):
            memo[i][j] += max(memo[i-1][j], memo[i-1][j+1])

    print(f"Case {case}: {memo[r-1][0]}")