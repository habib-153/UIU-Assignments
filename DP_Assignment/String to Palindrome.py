def solve():
    s = input()
    n = len(s)

    memo = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    def string_to_palindrome(i, j):
        # Base cases
        if i >= j:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        if s[i] == s[j]:
            memo[i][j] = string_to_palindrome(i+1, j-1)
            return memo[i][j]

        # delete at i, delete at j, or delete both
        memo[i][j] = min(string_to_palindrome(i+1, j) + 1, string_to_palindrome(i, j-1) + 1, string_to_palindrome(i+1, j-1) + 1)
        return memo[i][j]

    result = string_to_palindrome(0, n-1)
    print(f"Case {cnt}: {result}")

t = int(input())
cnt = 1

for _ in range(t):
    solve()
    cnt += 1