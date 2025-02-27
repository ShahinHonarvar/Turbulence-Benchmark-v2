import sympy

def is_left_right_truncatable(n):
    s = str(n)
    for i in range(len(s) - 1):
        if not sympy.isprime(int(s[i + 1:])) or not sympy.isprime(int(s[:-i - 1])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[630]
    primes = [p for p in sympy.primerange(2, x + 1) if '0' not in str(p) and is_left_right_truncatable(p)]
    return sorted(primes, reverse=True)