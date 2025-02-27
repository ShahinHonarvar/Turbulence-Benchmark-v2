import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[97]
    truncatable_primes = []
    for i in range(2, x):
        is_truncatable = True
        for j in range(len(str(i))):
            if not is_prime(int(str(i)[j:])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)