from math import gcd

def gcf_three_nums(nums):
    a = nums[8]
    b = nums[2]
    c = nums[1]
    return gcd(gcd(a, b), c)