from itertools import chain

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[38]
    truncatable_primes = []

    def has_zero(str_n):
        return '0' in str_n

    def generate_candidates(str_n):
        if len(str_n) <= 1 or not all_left_truncatable_prime.cache.get(str_n, False):
            return []
        return [int(str_n)]
    all_left_truncatable_prime.cache = {}
    primes = (str(n) for n in range(x) if is_prime(n) and (not has_zero(str(n))))
    for prime_str in sorted(primes, reverse=True):
        truncatable_primes.extend(generate_candidates(prime_str))
    return sorted(set(truncatable_primes), reverse=True)