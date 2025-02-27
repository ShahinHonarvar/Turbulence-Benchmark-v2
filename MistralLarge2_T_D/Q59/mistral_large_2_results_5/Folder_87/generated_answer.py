def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            if n < 10 and (not is_prime(n)):
                return False
            n //= 10
        return True
    x = numbers[39]
    left_truncatable_primes = [n for n in range(2, x) if '0' not in str(n) and is_left_truncatable_prime(n)]
    return sorted(left_truncatable_primes, reverse=True)