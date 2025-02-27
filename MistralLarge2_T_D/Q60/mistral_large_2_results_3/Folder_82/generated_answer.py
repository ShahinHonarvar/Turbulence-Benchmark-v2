import sympy

def is_left_right_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    if not sympy.isprime(n):
        return False
    while len(n_str) > 1:
        n_str = n_str[1:-1]
        if not n_str or not sympy.isprime(int(n_str)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[69]
    primes = [p for p in range(2, x + 1) if is_left_right_truncatable_prime(p)]
    return sorted(primes, reverse=True)