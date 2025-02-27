from sympy import isprime

def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:-i])):
                return False
        return True
    x = nums[370]
    result = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(result, reverse=True)