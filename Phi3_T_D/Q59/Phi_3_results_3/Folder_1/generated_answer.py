def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(prime):
        if not str(prime).startswith(('2', '3', '5', '7')):
            return False
        while prime > 0:
            if not is_prime(prime):
                return False
            prime //= 10
        return True
    x = numbers[20]
    left_truncatable_primes = [p for p in range(2, x) if is_left_truncatable_prime(p)]
    return left_truncatable_primes[::-1]