import math

def gcf_three_nums(nums):
    if len(nums) >= 100:
        a = nums[99]
        b = nums[95]
        c = nums[80]
        return math.gcd(math.gcd(a, b), c)
    else:
        raise ValueError('The list must have at least 100 elements.')