from sympy import isprime

def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(527, 539):
        if not isprime(nums[i]) and nums[i] > 1:
            composite_set.add(nums[i])
    return composite_set