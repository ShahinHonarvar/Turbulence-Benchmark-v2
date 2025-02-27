from sympy import isprime

def is_left_right_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    while len(s) > 1:
        if not isprime(int(s)):
            return False
        s = s[1:-1]
    return isprime(int(s))

def all_left_right_truncatable_prime(numbers):
    x = numbers[433]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)