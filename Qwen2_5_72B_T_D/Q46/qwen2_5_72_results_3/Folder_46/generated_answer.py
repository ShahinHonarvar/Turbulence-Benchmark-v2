from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[78], nums[19], nums[13])
    return gcd(gcd(a, b), c)