from sympy import isprime

def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if i >= 639 and i <= 975 and (not isprime(num))}