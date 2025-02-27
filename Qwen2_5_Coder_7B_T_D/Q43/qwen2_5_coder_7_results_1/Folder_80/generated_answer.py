import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [num for num in lst[13:30] if is_prime(num)]
    return sorted(primes, reverse=True)