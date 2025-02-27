def all_left_truncatable_prime(primes_tuple):
    x = primes_tuple[41]
    primes = set(primes_tuple)
    result = []

    def is_left_truncatable(n):
        while n > 0:
            if n not in primes:
                return False
            n = n // 10
        return True
    for n in primes:
        if n < x and is_left_truncatable(n):
            result.append(n)
            result.sort()
    return result