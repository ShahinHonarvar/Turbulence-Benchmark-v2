def all_left_right_truncatable_prime(numbers):
    x = numbers[65]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(prime):
        str_prime = str(prime)
        for length in range(1, len(str_prime)):
            if not is_prime(int(str_prime[length:])) or not is_prime(int(str_prime[:length])):
                return False
        return True
    left_right_truncatable_primes = [p for p in range(2, x + 1) if is_prime(p) and is_truncatable(p)]
    return sorted(left_right_truncatable_primes, reverse=True)