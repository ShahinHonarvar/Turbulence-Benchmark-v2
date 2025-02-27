from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[91]
    left_truncatable_primes = []
    for num in range(2, x):
        if all((isprime(int(str(num)[i:])) for i in range(len(str(num))))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)