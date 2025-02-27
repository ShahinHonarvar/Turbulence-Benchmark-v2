def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(prime):
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:-i])):
                return False
        return True
    x = numbers[41]
    truncatable_primes = [p for p in range(2, x + 1) if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)