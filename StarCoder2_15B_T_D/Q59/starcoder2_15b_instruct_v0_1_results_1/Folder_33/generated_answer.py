def all_left_truncatable_prime(numbers):
    x = numbers[945]

    def is_left_truncatable_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = [p for p in range(2, x) if is_left_truncatable_prime(p)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes