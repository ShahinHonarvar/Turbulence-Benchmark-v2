import sympy

def is_left_right_truncatable_prime(n):
    digits = str(n)
    if '0' in digits:
        return False
    for i in range(len(digits)):
        left_truncated = int(digits[i:])
        right_truncated = int(digits[:len(digits) - i])
        if not sympy.isprime(left_truncated) or not sympy.isprime(right_truncated):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[78]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)