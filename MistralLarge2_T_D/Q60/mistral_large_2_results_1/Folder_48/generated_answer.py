import sympy

def is_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if not sympy.isprime(int(s[i:])) or not sympy.isprime(int(s[:len(s) - i])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[835]
    primes = [p for p in sympy.primerange(1, x + 1) if '0' not in str(p)]
    truncatable_primes = [p for p in primes if is_truncatable_prime(p)]
    return sorted(truncatable_primes)