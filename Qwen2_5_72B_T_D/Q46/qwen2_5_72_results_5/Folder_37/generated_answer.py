from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[41], nums[69], nums[28])
    return gcd(gcd(a, b), c)