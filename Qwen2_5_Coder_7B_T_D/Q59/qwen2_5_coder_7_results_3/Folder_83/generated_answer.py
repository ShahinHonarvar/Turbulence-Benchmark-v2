from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[24]

    def is_left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if str_n[i] == '0' or not isprime(int(str_n[i:])):
                return False
        return True
    left_truncatable_primes = [n for n in range(2, x) if isprime(n) and is_left_truncatable(n)]
    return sorted(left_truncatable_primes)