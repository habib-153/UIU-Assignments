def isPrime(n):
    if n <=1:
        return False
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True

def generate_prime_powers(n):
    prime_powers = {}
    for i in range(2, n + 1):
        if isPrime(i):
            powers = []
            for j in range(3, n):
                if isPrime(j):
                    result = i ** j
                    if result < 100: 
                        powers.append(result)
            if powers:
                prime_powers[i] = powers

    return prime_powers

n = int(input())
# n= 10
output = generate_prime_powers(n)
print(output)