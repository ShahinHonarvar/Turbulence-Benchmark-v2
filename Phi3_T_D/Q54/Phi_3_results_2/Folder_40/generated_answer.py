import sympy

def all_right_truncatable_prime(limits):
    x = limits[10]
    truncatable_primes = []

    def is_right_truncatable_prime(n):
        while n > 0:
            if not sympy.isprime(n):
                return False
            n = n // 10
        return True
    for candidate in range(2, x):
        if is_right_truncatable_prime(candidate):
            truncatable_primes.insert(0, candidate)
    return sorted(truncatable_primes)