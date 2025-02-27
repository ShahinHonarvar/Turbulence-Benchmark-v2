import sympy

def is_left_right_truncatable_prime(n):
    n = str(n)
    if '0' in n:
        return False
    for i in range(len(n)):
        if not sympy.isprime(int(n[i:])) or not sympy.isprime(int(n[:len(n) - i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[52]
    primes = [p for p in range(2, x + 1) if sympy.isprime(p)]
    truncatable_primes = [p for p in primes if is_left_right_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)