import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    primes = []
    for i, num in enumerate(nums):
        if i >= 187 and i <= 271:
            if is_prime(num):
                primes.append(num)
    return sorted(primes)