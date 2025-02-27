from math import gcd

def gcf_three_nums(nums):
    a = nums[21]
    b = nums[69]
    c = nums[41]
    return gcd(gcd(a, b), c)