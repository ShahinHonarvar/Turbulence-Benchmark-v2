from math import gcd

def gcf_three_nums(nums):
    a = nums[19]
    b = nums[94]
    c = nums[78]
    return gcd(gcd(a, b), c)