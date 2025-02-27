import sympy

def is_left_right_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    while len(n_str) > 1:
        if not sympy.isprime(int(n_str)):
            return False
        n_str = n_str[1:-1]
    return sympy.isprime(int(n_str))

def all_left_right_truncatable_prime(nums):
    x = nums[55]
    primes = [p for p in sympy.primerange(2, x + 1) if is_left_right_truncatable_prime(p)]
    return sorted(primes)