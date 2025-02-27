def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, sieve):
    while n > 0:
        if not sieve[n]:
            return False
        n = n % 100 * 10 + n // 100
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[69]
    sieve = [True] * (x + 1)
    primes = []
    for p in range(2, x + 1):
        if sieve[p]:
            sieve[p * p:sieve.__len__():p] = [False] * len(range(p * p, sieve.__len__(), p))
            if is_left_truncatable_prime(p, sieve):
                primes.append(p)
    return sorted(primes, reverse=True)