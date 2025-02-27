from math import gcd

def gcf_three_nums(nums):
    a = nums[38]
    b = nums[52]
    c = nums[69]
    return gcd(gcd(a, b), c)