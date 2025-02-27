def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable_prime(n, sieve):
        return all((d in sieve and is_prime(int(str(n)[:i])) for i, d in enumerate(str(n), 1)))
    x = numbers[73]
    sieve = set(filter(is_prime, range(2, x)))
    left_truncatable_primes = set()
    right_truncatable_primes = set()
    for prime in sieve:
        left_truncatable_primes.add(prime)
        if is_right_truncatable_prime(prime, sieve):
            right_truncatable_primes.add(prime)
    return sorted(right_truncatable_primes, reverse=True)