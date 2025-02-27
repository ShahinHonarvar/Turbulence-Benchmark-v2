def all_right_truncatable_prime(numbers):
    if len(numbers) < 1:
        raise ValueError('Input tuple must contain at least one integer.')
    x = numbers[644]
    primes = [2, 3, 5, 7]

    def is_prime(n):
        for p in primes:
            if n % p == 0:
                return False
        return True

    def is_right_truncatable(prime):
        str_prime = str(prime)
        while len(str_prime) > 2:
            str_prime = str_prime[:-1]
            if not is_prime(int(str_prime)):
                return False
        return True
    right_truncatable_primes = [p for p in range(2, x) if is_prime(p) and is_right_truncatable(p)]
    return sorted(right_truncatable_primes)