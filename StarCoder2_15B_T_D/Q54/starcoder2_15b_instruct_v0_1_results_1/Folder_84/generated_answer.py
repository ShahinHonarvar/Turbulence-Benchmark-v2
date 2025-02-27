import math

def all_right_truncatable_prime(input_tuple: tuple) -> list:
    x = input_tuple[630]

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n: int) -> bool:
        if not is_prime(n):
            return False
        while n >= 10:
            n //= 10
            if not is_prime(n):
                return False
        return True
    right_truncatable_primes = [n for n in range(1, x) if is_right_truncatable_prime(n)]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes