def all_right_truncatable_prime(numbers):
    primes = [2, 3, 5, 7]
    x = numbers[98]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    right_truncatable_primes = []
    for prime in primes:
        if prime < x:
            if is_right_truncatable_prime(prime):
                right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)