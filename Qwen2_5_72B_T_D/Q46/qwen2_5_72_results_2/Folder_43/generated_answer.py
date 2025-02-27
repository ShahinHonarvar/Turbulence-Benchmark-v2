from math import gcd

def gcf_three_nums(nums):
    a = nums[33]
    b = nums[78]
    c = nums[93]
    return gcd(gcd(a, b), c)