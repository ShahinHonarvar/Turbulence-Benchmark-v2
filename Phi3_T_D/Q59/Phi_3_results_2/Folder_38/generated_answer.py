def all_left_truncatable_prime(numbers):
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[28]
    left_truncatable_primes = []
    for prime in primes:
        if prime < x and is_left_truncatable_prime(prime):
            left_truncatable_primes.append(prime)
    return left_truncatable_primes