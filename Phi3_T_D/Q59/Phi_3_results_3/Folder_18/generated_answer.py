from sympy import isprime

def is_left_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not isprime(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_truncatable_prime(nums):
    x = nums[428]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)