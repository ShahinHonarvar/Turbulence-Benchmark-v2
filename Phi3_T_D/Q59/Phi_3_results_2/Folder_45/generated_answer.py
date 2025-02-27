from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[61]
    truncable_primes = []
    for num in range(2, x):
        if num < 10 and isprime(num):
            truncable_primes.append(num)
        elif isprime(num) and all((isprime(num // 10 ** i % 10 ** len(str(num))) for i in range(len(str(num)) - 1))):
            truncable_primes.append(num)
    return truncable_primes