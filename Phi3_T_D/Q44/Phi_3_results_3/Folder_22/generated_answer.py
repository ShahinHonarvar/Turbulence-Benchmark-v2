from sympy import isprime

def composite_nums_between_indices(nums):
    return {num for num in nums[50:201] if not isprime(num) and num != 1}