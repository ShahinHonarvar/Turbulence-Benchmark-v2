from math import gcd

def gcf_three_nums(nums):
    a = nums[56]
    b = nums[54]
    c = nums[13]
    return gcd(gcd(a, b), c)