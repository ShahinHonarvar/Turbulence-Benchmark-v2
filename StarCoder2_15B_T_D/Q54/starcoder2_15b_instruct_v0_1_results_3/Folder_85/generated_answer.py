import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    right_truncatable_primes = []
    for num in nums:
        if is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)