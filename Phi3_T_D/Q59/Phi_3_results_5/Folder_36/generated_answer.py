from itertools import product

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n % 10 ** len(str(n))
    return True

def all_left_truncatable_prime(nums):
    upper_limit = nums[992]
    truncatable_primes = []
    for digits in product([1, 3, 7, 9], repeat=len(str(upper_limit))):
        number = sum((d * 10 ** i for i, d in enumerate(digits)))
        if is_prime(number) and is_left_truncatable_prime(number):
            truncatable_primes.append(number)
    return sorted(truncatable_primes)