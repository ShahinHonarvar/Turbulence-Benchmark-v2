from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[695], nums[710], nums[914])
    return gcd(gcd(a, b), c)