from sympy import isprime

def is_left_right_truncatable_prime(n):
    if not isprime(n) or '0' in str(n):
        return False
    n_str = str(n)
    while len(n_str) > 1:
        n_str = n_str[1:-1]
        if not isprime(int(n_str)) or '0' in n_str:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[42]
    primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(primes)