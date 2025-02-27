def all_left_truncatable_prime(numbers):
    x = numbers[32]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, primes_cache):
        if n not in primes_cache:
            return False
        str_n = str(n)
        return all((is_left_truncatable(int(str_n[:i]), primes_cache) for i in range(1, len(str_n))))
    primes_cache = {2, 3, 5, 7}
    for prime in range(11, x, 2):
        if all((prime % d != 0 for d in range(3, int(prime ** 0.5) + 1, 2))):
            str_prime = str(prime)
            primes_cache.add(prime)
            if is_left_truncatable(prime, primes_cache):
                yield prime