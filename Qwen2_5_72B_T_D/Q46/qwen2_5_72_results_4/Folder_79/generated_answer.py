from math import gcd

def gcf_three_nums(nums):
    a = nums[16]
    b = nums[87]
    c = nums[95]
    return gcd(gcd(a, b), c)