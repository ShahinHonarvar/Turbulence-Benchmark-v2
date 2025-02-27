import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[31]
    left_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all((is_prime(int(num_str[:i])) for i in range(1, len(num_str) + 1))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)