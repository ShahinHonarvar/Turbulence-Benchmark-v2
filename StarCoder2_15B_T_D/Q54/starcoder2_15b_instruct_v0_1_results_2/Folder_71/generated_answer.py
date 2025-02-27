import math

def all_right_truncatable_prime(numbers):
    x = numbers[22]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 9:
            n //= 10
            if not is_prime(n):
                return False
        return True
    right_truncatable_primes = [p for p in range(2, x) if is_right_truncatable_prime(p)]
    return sorted(right_truncatable_primes, reverse=True)