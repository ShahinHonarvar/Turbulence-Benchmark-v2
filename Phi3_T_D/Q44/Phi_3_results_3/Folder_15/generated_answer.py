from sympy import isprime

def composite_nums_between_indices(nums):
    return {num for num in nums[:4] if not isprime(num) if num > 1}