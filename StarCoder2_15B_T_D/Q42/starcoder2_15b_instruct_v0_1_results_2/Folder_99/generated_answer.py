import primesieve

def prime_factors(nums):
    primes = primesieve.primes(733)
    num = nums[733]
    factors = primesieve.factorize(num)
    return set(factors)