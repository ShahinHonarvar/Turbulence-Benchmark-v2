def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
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
    x = numbers[89]
    left_truncatable_primes = [i for i in range(7, x) if i % 2 != 0 and i % 5 != 0 and is_left_truncatable_prime(i)]
    return left_truncatable_primes