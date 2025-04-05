from math import sqrt

n, m = map(int, input().split())
k = int(input())
points = []
for _ in range(k):
    x, y = map(int, input().split())
    points.append((x, y))

# Sort points by both coordinates
points.sort()

memo = [[-1] * (k + 1) for _ in range(k)]

def longest_increasing_subsequence(idx, prev_idx):
    # Base case: reached the beginning
    if idx < 0:
        return 0
        
    # Return memoized result if available
    if memo[idx][prev_idx] != -1:
        return memo[idx][prev_idx]
    
    # Option 1: Skip current element
    result = longest_increasing_subsequence(idx - 1, prev_idx)
    
    # Option 2: Include current element if it forms an increasing sequence
    if prev_idx == k or (points[idx][0] < points[prev_idx][0] and points[idx][1] < points[prev_idx][1]):
        result = max(result, 1 + longest_increasing_subsequence(idx - 1, idx))
    
    # Store in memo array and return
    memo[idx][prev_idx] = result
    return result

# Find the maximum length of increasing subsequence
mx = longest_increasing_subsequence(k-1, k) if k > 0 else 0

# Calculate final result
res = ((n + m) - 2 * mx) * 100 + sqrt(2.0) * mx * 100
print(int(round(res)))