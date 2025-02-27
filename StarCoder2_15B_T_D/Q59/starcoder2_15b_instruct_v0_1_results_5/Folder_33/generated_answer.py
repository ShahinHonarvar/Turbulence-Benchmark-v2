import math

def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n //= 10
            if not is_prime(n):
                return False
        return True
    x = numbers[945]
    left_truncatable_primes = [p for p in range(2, x) if is_left_truncatable_prime(p)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes