from sympy import isprime

def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums[90:201], start=90) if not isprime(num) and num > 1}