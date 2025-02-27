from sympy import isprime

def is_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    for i in range(len(n_str)):
        if not isprime(int(n_str[i:])) or not isprime(int(n_str[:len(n_str) - i])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[23]
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes)