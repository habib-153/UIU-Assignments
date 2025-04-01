"""
########################## EDITORIAL#####################################
red band band can be place after white and after those blue band which come after white band ..
simalarly for placing  white we can place after any red band or after blue band which come after red band .. so that we maintane 2   different block for blue band 1 for which come after white band and other for which comes after red band .. and its value update according to privious no of red or white band(corresponding to different blue bands)...
and finally ans is obtain by red band and white band since last band cant be blue ...."
"""
#################################### CODE#######################################

def count_ways(n):
    # memo[i][j] represents the number of ways to arrange i bands ending with color j
    # red=0, blue_after_red=1, blue_after_white=2, white=3
    memo = [[0 for _ in range(4)] for _ in range(n+1)]

    if n == 1 or n == 2:
        return 2

    memo[1][0] = 1
    memo[1][3] = 1
    for i in range(2, n):
        memo[i][0] = memo[i-1][2] + memo[i-1][3]
        memo[i][1] = memo[i-1][0]
        memo[i][2] = memo[i-1][3]
        memo[i][3] = memo[i-1][0] + memo[i-1][1]
    memo[n][0] = memo[n-1][2] + memo[n-1][3]
    memo[n][3] = memo[n-1][0] + memo[n-1][1]

    # print(memo)
    return memo[n][0] + memo[n][3]


if __name__ == "__main__":
    n = int(input())
    print(count_ways(n))
