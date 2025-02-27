from sympy import isprime

def is_left_right_truncatable_prime(n):
    if n < 10:
        return isprime(n)
    s = str(n)
    if '0' in s:
        return False
    left = 0
    right = len(s) - 1
    while left < right:
        if not isprime(int(s[left:right + 1])):
            return False
        left += 1
        right -= 1
    return isprime(int(s[left]))

def all_left_right_truncatable_prime(nums):
    x = nums[30]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)], reverse=True)