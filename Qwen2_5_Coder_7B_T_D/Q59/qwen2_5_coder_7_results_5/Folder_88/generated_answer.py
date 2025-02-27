from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[93]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i) and all((isprime(int(str(i)[j:])) for j in range(len(str(i))))):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)