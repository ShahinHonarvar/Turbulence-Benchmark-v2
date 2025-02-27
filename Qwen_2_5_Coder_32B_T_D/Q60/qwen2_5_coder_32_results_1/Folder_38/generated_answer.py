from sympy import isprime

def all_left_right_truncatable_prime(nums):

    def is_lr_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 1:
            if not isprime(int(s[1:])) or not isprime(int(s[:-1])):
                return False
            s = s[1:-1]
        return True
    x = nums[28]
    lr_trunc_primes = []
    for num in range(10, x + 1):
        if is_lr_truncatable_prime(num):
            lr_trunc_primes.append(num)
    return lr_trunc_primes