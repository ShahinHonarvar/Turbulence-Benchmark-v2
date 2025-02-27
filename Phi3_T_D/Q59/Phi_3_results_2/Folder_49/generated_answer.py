def all_left_truncatable_prime(numeric_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, sieve):
        while n > 0:
            n, d = divmod(n, 10)
            if n == 0 and (not is_prime(d)) or d == 0 or (not sieve[d]):
                return False
        return True
    x = numeric_tuple[14]
    primes = [2, 3, 5, 7]
    prime_set = set(primes)
    max_prime = int('9' * len(str(x)))
    while primes[-1] < max_prime:
        p = primes[-1] + 2
        if p >= x:
            break
        if is_prime(p):
            prime_set.add(p)
            primes.append(p)
    return [p for p in primes if is_left_truncatable(p, prime_set)]