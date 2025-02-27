def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, sieve):
        while n > 0:
            if not sieve[n]:
                return False
            n = n % 10 ** len(str(n))
        return True
    x = numbers[26]
    max_len = len(str(x))
    sieve = [True] * (x + 1)
    primes = [i for i in range(2, x + 1) if is_prime(i) and i > 2]
    for prime in primes:
        if prime > max_len:
            break
        for p in range(prime, x + 1, prime):
            sieve[p] = False
    left_truncatables = [prime for prime in primes if is_left_truncatable(prime, sieve)]
    return left_truncatables