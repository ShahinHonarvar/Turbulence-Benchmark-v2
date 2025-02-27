import math

def all_right_truncatable_prime(nums):
    x = nums[94]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    right_truncatable_primes = [p for p in range(2, x) if is_right_truncatable_prime(p)]
    return sorted(right_truncatable_primes)