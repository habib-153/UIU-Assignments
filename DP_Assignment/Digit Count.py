q = int(input())
for t in range(1, q + 1):
    n, m = map(int, input().split())
    dp = list(map(int, input().split()))
    a = [[0 for _ in range(10)] for _ in range(m + 1)]
    for j in range(n):
        a[1][dp[j]] = 1
    for j in range(1, m + 1):
        for i in range(n):
            for x in range(-2, 3):
                k = dp[i] + x
                if 10 > k > 0:
                    a[j][dp[i]] += a[j - 1][k]
    result = 0
    for k in dp:
        result += a[m][k]
    print(f"Case {t}: {result}")
