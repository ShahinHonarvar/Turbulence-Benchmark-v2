import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    start_index = 28
    end_index = 44
    primes = []
    for i, n in enumerate(lst):
        if is_prime(n) and start_index <= i <= end_index:
            primes.append(n)
    return sorted(primes)