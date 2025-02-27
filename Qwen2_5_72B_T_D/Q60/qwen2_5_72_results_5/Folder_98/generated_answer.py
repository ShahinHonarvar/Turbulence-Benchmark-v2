from sympy import isprime

def all_left_right_truncatable_prime(nums):
    x = nums[8]

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while len(str_n) > 1:
            if not isprime(int(str_n)):
                return False
            str_n = str_n[1:-1]
        return isprime(int(str_n))
    return [n for n in range(x, 1, -1) if is_left_right_truncatable_prime(n)]