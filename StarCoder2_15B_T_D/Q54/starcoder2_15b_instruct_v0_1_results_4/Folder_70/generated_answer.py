import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def generate_right_truncatable_primes(x):
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return right_truncatable_primes

def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[433]
    right_truncatable_primes = generate_right_truncatable_primes(x)
    right_truncatable_primes.sort(reverse=True)
    if right_truncatable_primes:
        return right_truncatable_primes
    else:
        return []