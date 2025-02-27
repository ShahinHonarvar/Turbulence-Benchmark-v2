import sympy

def is_truncatable_prime(n):
    if not sympy.isprime(n):
        return False
    if '0' in str(n):
        return False
    s = str(n)
    for i in range(1, len(s)):
        if not sympy.isprime(int(s[i:])) or not sympy.isprime(int(s[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[975]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)