from sympy import primefactors

def prime_factors(nums):
    if 247 < len(nums):
        return set(primefactors(nums[247]))
    else:
        return 'Index out of range'