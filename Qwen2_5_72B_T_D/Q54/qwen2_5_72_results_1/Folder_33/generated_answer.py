from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[945]

    def is_right_truncatable_prime(n):
        while n:
            if not isprime(n):
                return False
            n //= 10
        return True
    return sorted([i for i in range(x, 1, -1) if is_right_truncatable_prime(i)])