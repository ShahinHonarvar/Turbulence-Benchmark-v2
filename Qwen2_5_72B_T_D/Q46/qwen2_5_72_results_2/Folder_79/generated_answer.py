from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[16], nums[87], nums[95])
    return gcd(gcd(a, b), c)