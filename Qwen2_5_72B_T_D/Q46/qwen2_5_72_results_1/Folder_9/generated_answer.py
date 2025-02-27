from math import gcd

def gcf_three_nums(nums):
    a = nums[66]
    b = nums[90]
    c = nums[27]
    return gcd(gcd(a, b), c)