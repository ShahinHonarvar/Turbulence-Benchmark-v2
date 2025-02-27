from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[30]

    def is_left_truncatable_prime(n):
        s = str(n)
        for i in range(1, len(s) + 1):
            if not isprime(int(s[i - 1:])):
                return False
        return True
    return [n for n in range(2, x) if is_left_truncatable_prime(n)]