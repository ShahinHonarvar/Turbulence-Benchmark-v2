from sympy import isprime

def all_left_truncatable_prime(nums):
    base, x = (10, nums[23])
    truncatable_primes = [i for i in range(2, x) if isprime(i)]
    for p in truncatable_primes[:]:
        n = p
        while n > 0:
            if not isprime(n):
                truncatable_primes.remove(p)
                break
            n //= base
    return sorted(truncatable_primes)