from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[14], nums[21], nums[17])
    return gcd(gcd(a, b), c)