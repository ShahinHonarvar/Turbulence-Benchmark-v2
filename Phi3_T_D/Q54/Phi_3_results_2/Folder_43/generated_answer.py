def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes_map):
    original_n = n
    while n > 0:
        if not is_prime(n):
            return False
        if n not in primes_map:
            return False
        n //= 10
    return n == 0

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[89]
    primes = set(filter(is_prime, range(2, x)))
    primes_map = {p: p for p in primes}
    right_truncatables = []
    for prime in sorted(primes, reverse=True):
        if is_right_truncatable_prime(prime, primes_map):
            right_truncatables.append(prime)
    return right_truncatables