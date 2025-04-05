for test_case in range(int(input())):
    n, modulo = map(int, input().split())
    numbers = list(map(int, input().split()))
    remainders = {numbers[0] % modulo}
    for i in range(n-1):
        temp_set = remainders.copy()
        remainders.clear()
        for j in temp_set:
            remainders.add((j+numbers[i+1]) % modulo)
            remainders.add((j-numbers[i+1]) % modulo)
        zero_set = {0}
        if (len(remainders.intersection(zero_set))):
            print("Divisible")
        else:
            print("Not divisible")