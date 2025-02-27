import sympy

def is_left_right_truncatable_prime(n):
    if not sympy.isprime(n):
        return False
    s = str(n)
    if '0' in s:
        return False
    for i in range(len(s) - 1):
        if not sympy.isprime(int(s[i + 1:])):
            return False
        if not sympy.isprime(int(s[:len(s) - i - 1])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[87]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(truncatable_primes)