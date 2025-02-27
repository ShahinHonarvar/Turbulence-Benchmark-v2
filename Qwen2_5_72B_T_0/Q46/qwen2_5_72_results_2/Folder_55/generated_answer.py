from math import gcd

def gcf_three_nums(nums):
    a = nums[2]
    b = nums[6]
    c = nums[9]
    return gcd(gcd(a, b), c)