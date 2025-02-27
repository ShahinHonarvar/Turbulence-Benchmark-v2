from math import gcd

def gcf_three_nums(nums):
    a = nums[19]
    b = nums[69]
    c = nums[97]
    return gcd(gcd(a, b), c)