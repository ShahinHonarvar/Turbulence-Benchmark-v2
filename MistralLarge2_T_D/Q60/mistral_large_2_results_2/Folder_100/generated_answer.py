from sympy import isprime

def all_left_right_truncatable_prime(nums):

    def is_left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:len(s) - i])):
                return False
        return True
    x = nums[26]
    return sorted([n for n in range(2, x + 1) if isprime(n) and is_left_right_truncatable(n)])