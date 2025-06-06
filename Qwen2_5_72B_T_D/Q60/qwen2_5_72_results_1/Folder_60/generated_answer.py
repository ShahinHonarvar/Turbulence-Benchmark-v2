from sympy import isprime

def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:-i])):
                return False
        return isprime(n)
    x = nums[87]
    return [n for n in range(2, x + 1) if is_truncatable_prime(n)]