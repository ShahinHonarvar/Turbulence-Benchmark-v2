import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[97]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num) or not is_prime(num):
            continue
        is_left_truncatable = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)