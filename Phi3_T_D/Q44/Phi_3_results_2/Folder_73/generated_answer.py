from sympy import isprime

def composite_nums_between_indices(nums):
    composites = set()
    for i in range(28, 41):
        if not isprime(nums[i]) and nums[i] > 1:
            composites.add(nums[i])
    return composites