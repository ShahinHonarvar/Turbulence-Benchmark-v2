import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[100]
    left_truncatable_primes = []
    for p in range(2, x):
        if is_prime(p):
            is_left_truncatable = True
            for i in range(len(str(p)) - 1):
                if not is_prime(int(str(p)[i + 1:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(p)
    left_truncatable_primes.sort()
    return left_truncatable_primes