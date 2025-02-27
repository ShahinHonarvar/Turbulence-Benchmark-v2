from math import gcd

def gcf_three_nums(nums):
    x = nums[990]
    y = nums[671]
    z = nums[711]
    return gcd(x, gcd(y, z))