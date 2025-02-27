from math import gcd

def gcf_three_nums(nums):
    a = nums[654]
    b = nums[312]
    c = nums[441]
    return gcd(gcd(a, b), c)