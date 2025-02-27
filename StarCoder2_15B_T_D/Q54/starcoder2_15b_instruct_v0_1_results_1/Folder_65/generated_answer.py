from math import sqrt

def all_right_truncatable_prime(t):
    x = t[32]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n //= 10
            if not is_prime(n):
                return False
        return True
    return sorted((n for n in range(2, x) if is_right_truncatable_prime(n)))