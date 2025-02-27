import math

def all_left_truncatable_prime(x):
    x = x[0]
    primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    left_truncatable_primes = []
    for prime in primes:
        is_left_truncatable = True
        num = prime
        while num > 0:
            num = num // 10
            if num == 0:
                break
            is_left_truncatable = True
            for j in range(2, int(math.sqrt(num)) + 1):
                if num % j == 0:
                    is_left_truncatable = False
                    break
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes