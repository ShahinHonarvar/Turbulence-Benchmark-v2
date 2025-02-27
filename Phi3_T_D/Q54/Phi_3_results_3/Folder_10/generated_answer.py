def all_right_truncatable_prime(numbers):
    x = numbers[38]
    primes = [2, 3, 5, 7]
    rt_primes = []

    def is_prime(n):
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True

    def truncate(n):
        return n // 10 if n > 0 else None

    def extend_primes(prime):
        if prime > x:
            return
        primes.append(prime)
        n = truncate(prime)
        while n is not None:
            shorter = n * 10 + prime % 10
            if is_prime(shorter):
                truncate(shorter)
            else:
                break
    for prime in primes:
        extend_primes(prime)
    rt_primes = [p for p in primes if is_prime(p) and truncate(p) is not None]
    return sorted(rt_primes, reverse=True)