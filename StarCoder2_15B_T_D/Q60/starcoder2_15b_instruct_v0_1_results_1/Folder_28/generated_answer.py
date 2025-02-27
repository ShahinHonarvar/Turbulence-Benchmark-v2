import math

def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
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

    def is_left_truncatable_prime(n):
        while n >= 10:
            if not is_prime(n):
                return False
            n //= 10
        return is_prime(n)
    x = numbers[19]
    return sorted((n for n in range(2, x + 1) if is_left_truncatable_prime(n) and is_prime(n)))