from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[4]

    def is_left_truncatable_prime(n):
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
        return True
    return [n for n in range(2, x) if is_left_truncatable_prime(n)]