def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        return all((is_prime(int(str(n)[:i])) and is_prime(int(str(n)[-i:])) for i in range(1, len(str(n)))))
    threshold = numbers[22]
    truncatable_primes = [p for p in range(2, threshold + 1) if is_prime(p) and is_left_right_truncatable(p)]
    return sorted(truncatable_primes, reverse=True)