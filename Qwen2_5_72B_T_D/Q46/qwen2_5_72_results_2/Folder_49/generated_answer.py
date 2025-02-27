from math import gcd

def gcf_three_nums(nums):
    a = nums[34]
    b = nums[38]
    c = nums[77]
    return gcd(gcd(a, b), c)