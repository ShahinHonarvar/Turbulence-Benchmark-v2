from sympy import primerange

def is_left_and_right_truncatable_prime(n, prime_set):
    if n not in prime_set:
        return False
    n_str = str(n)
    for i in range(1, len(n_str) // 2 + 1):
        if int(n_str[i:]) not in prime_set or int(n_str[:-i]) not in prime_set:
            return False
    return True

def all_left_and_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[992]
    primes = set(primerange(0, x + 1))
    return sorted((p for p in primes if is_left_and_right_truncatable_prime(p, primes)))