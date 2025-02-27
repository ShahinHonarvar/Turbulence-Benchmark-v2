from math import gcd

def gcf_three_nums(nums):
    a = nums[4]
    b = nums[1]
    c = nums[7]
    return gcd(gcd(a, b), c)