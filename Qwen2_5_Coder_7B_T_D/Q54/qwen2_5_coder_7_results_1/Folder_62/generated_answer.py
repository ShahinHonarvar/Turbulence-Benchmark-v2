from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[70]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            str_num = str(num)
            while len(str_num) > 1:
                str_num = str_num[:-1]
                if not isprime(int(str_num)):
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)