def all_right_truncatable_prime(numbers):
    x = numbers[760]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(prime, n):
        while prime > 0:
            if not is_prime(prime):
                return False
            prime //= 10
        return True
    right_truncatables = [prime for prime in range(x, 1, -1) if is_right_truncatable(prime, prime) and is_prime(prime)]
    return right_truncatables