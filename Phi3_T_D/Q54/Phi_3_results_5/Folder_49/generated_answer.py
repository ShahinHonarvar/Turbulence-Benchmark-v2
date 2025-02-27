def all_right_truncatable_prime(numbers):
    max_val = numbers[14]

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
    primes = [n for n in range(2, max_val) if is_right_truncatable_prime(n)]
    return primes