from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[3]

    def is_left_truncatable_prime(n):
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    return [n for n in range(x - 1, 1, -1) if isprime(n) and '0' not in str(n) and is_left_truncatable_prime(n)]