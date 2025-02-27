def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_prime(n):
        n = str(n)
        while len(n) > 1:
            if not is_prime(int(n)):
                return False
            n = n[1:-1]
        return is_prime(int(n))
    x = numbers[11]
    truncatable_primes = [p for p in range(2, x + 1) if is_left_right_prime(p)]
    return truncatable_primes