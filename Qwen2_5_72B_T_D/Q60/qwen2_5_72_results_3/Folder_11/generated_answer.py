import sympy

def all_left_right_truncatable_prime(nums):
    x = nums[86]

    def is_truncatable_prime(n):
        if not sympy.isprime(n) or '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s)):
            if not sympy.isprime(int(s[i:])) or not sympy.isprime(int(s[:-i])):
                return False
        return True
    return [i for i in range(2, x + 1) if is_truncatable_prime(i)]