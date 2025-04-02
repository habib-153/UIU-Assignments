def paint(costs):
    if not costs:
        return 0

    n = len(costs)
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0] = costs[0]

    for i in range(1, n):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

    return min(dp[n-1])

for n in range(int(input())):
    input()  
    cost = [list(map(int, input().split())) for _ in range(int(input()))]
    print(f"Case {n+1}: {paint(cost)}")