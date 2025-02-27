from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[64]
    right_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        if all((isprime(int(str_num[:i + 1])) for i in range(len(str_num)))):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)