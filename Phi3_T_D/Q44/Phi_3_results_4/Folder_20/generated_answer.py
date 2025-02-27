from sympy import isprime

def composite_nums_between_indices(nums):
    return {n for n in nums[74:96] if not isprime(n)}