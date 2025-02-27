def all_right_truncatable_prime(numbers):
    x = numbers[54]
    limit = x
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

    def is_right_truncatable(n):
        while n > 0:
            if not sieve[n]:
                return False
            n //= 10
        return True
    right_truncatable_primes = [n for n in range(2, limit) if is_right_truncatable(n)]
    return sorted(right_truncatable_primes, reverse=True)