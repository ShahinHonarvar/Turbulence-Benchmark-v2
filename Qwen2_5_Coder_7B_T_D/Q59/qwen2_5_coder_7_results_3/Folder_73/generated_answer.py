from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[97]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num) and all((isprime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)