import math

def gcf_three_nums(nums):
    if len(nums) >= 77:
        return math.gcd(nums[15], nums[51], nums[76])
    else:
        raise IndexError('List must have at least 77 elements')