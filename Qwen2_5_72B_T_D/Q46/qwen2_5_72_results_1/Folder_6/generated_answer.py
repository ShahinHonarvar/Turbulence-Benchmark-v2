from math import gcd

def gcf_three_nums(nums):
    a = nums[93]
    b = nums[94]
    c = nums[57]
    return gcd(gcd(a, b), c)