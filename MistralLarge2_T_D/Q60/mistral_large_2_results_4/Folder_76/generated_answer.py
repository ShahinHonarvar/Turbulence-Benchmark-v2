import sympy

def is_left_right_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str or not sympy.isprime(n):
        return False
    for i in range(1, len(n_str)):
        if not sympy.isprime(int(n_str[i:])) or not sympy.isprime(int(n_str[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[370]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)