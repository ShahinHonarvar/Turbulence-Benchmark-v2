import math

def all_right_truncatable_prime(tup):
    x = tup[41]

    def is_right_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        if not is_prime(num):
            return False
        return is_right_truncatable_prime(int(num / 10))

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    right_truncatable_primes = [p for p in range(10, x) if is_right_truncatable_prime(p)]
    return sorted(right_truncatable_primes, reverse=True)