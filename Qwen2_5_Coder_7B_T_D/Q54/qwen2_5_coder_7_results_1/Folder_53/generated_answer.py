from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[86]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            str_num = str(num)
            while isprime(int(str_num)):
                str_num = str_num[:-1]
                if len(str_num) == 0:
                    right_truncatable_primes.append(num)
                    break
    return sorted(right_truncatable_primes, reverse=True)