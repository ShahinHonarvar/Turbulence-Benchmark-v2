from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[990], nums[671], nums[711])
    return gcd(gcd(a, b), c)