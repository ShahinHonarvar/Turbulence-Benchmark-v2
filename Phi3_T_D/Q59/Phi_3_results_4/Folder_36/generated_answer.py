from sympy import isprime

def all_left_truncatable_prime(number_tuple):
    x = number_tuple[992]
    truncatables = []

    def is_left_truncatable(n, primes_set):
        if n < 10:
            return False
        while n > 0:
            if not isprime(n) or n not in primes_set:
                return False
            n //= 10
        return True
    primes_set = set(filter(isprime, range(2, x)))
    for prime in primes_set:
        if is_left_truncatable(prime, primes_set):
            truncatables.append(prime)
    return sorted(truncatables)