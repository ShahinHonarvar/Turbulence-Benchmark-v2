import sympy

def is_right_truncatable_prime(n):
    while n > 0:
        if not sympy.isprime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[975]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)