import sympy

def prime_factors(nums):
    if len(nums) > 46:
        return sympy.primefactors(nums[46])
    else:
        raise IndexError('The list must contain at least 47 elements to access index 46.')