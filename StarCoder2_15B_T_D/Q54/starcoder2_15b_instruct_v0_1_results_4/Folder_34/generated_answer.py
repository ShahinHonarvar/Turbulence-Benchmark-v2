from math import sqrt

def all_right_truncatable_prime(nums):
    x = nums[18]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    return sorted(filter(is_right_truncatable_prime, range(2, x)), reverse=True)