def all_left_truncatable_prime(numbers):
    x = numbers[55]
    limit = x
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(limit ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
    primes = [i for i in range(2, limit) if sieve[i]]

    def is_left_truncatable_prime(n):
        while n > 0:
            if '0' in str(n) or not sieve[n]:
                return False
            n //= 10
        return True
    return sorted(filter(is_left_truncatable_prime, primes))