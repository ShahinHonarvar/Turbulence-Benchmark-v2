from sympy import isprime

def all_left_truncatable_prime(nums):

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n)) + 1):
            if not isprime(int(str(n)[:i])):
                return False
        return True
    x = nums[992]
    return [n for n in range(2, x) if is_left_truncatable_prime(n)]