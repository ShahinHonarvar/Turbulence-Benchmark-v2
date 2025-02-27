from sympy import primefactors

def prime_factors(nums):
    if len(nums) > 7:
        return set(primefactors(nums[7]))
    return set()