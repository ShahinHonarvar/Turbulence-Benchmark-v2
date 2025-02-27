from math import gcd

def gcf_three_nums(nums):
    a = nums[1]
    b = nums[6]
    c = nums[8]
    return gcd(gcd(a, b), c)