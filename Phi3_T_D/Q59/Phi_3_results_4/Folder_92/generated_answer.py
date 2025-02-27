from sympy import isprime

def all_left_truncatable_prime(nums):
    x = nums[7]
    primes = []
    for num in range(2, x):
        if all((isprime(int(str(num)[i:])) for i in range(len(str(num))))):
            primes.append(num)
    return primes