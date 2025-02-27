from sympy import isprime

def all_left_right_truncatable_prime(nums):

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[i:])) or not isprime(int(str(n)[:-i])):
                return False
        return True
    x = nums[11]
    return [n for n in range(2, x + 1) if isprime(n) and is_left_right_truncatable_prime(n)]