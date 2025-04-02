import sys

def main():
    elephants = []
    for line in sys.stdin:
        weight, iq = map(int, line.split())
        elephants.append((weight, iq, len(elephants) + 1))

    elephants.sort(key=lambda x: (x[0], -x[1]))

    n = len(elephants)
    memo = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if elephants[j][1] > elephants[i][1] and memo[j] + 1 > memo[i]:
                memo[i] = memo[j] + 1
                prev[i] = j

    best_idx = memo.index(max(memo))
    path = []
    while best_idx != -1:
        path.append(elephants[best_idx][2])
        best_idx = prev[best_idx]

    print(len(path))
    for idx in reversed(path):
        print(idx)

if __name__ == "__main__":
    main()