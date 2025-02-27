from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[10]
    left_truncatable_primes = []

    def is_left_truncatable(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return True
    for num in range(2, x):
        if '0' not in str(num) and is_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)

def is_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if not isprime(int(str_num[i:])):
            return False
    return isprime(num)