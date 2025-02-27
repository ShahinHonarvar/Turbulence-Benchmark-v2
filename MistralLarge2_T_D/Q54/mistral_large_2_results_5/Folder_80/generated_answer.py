from sympy import isprime

def all_right_truncatable_prime(nums):
    x = nums[14]
    primes = []

    def is_right_truncatable(n):
        while n:
            if not isprime(n):
                return False
            n //= 10
        return True
    for num in range(2, x):
        if is_right_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)