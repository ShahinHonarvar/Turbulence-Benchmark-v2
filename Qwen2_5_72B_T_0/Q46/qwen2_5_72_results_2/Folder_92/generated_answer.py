from math import gcd

def gcf_three_nums(nums):
    a = nums[0]
    b = nums[7]
    c = nums[9]
    return gcd(gcd(a, b), c)