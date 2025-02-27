import sympy

def all_left_truncatable_prime(nums):
    x = nums[94]
    left_truncatable_primes = []
    for number in range(10, x):
        if all((int(str(number)[i:]) % i == 0 for i in range(1, len(str(number))) if sympy.isprime(int(str(number)[i:])))):
            left_truncatable_primes.append(number)
    return left_truncatable_primes