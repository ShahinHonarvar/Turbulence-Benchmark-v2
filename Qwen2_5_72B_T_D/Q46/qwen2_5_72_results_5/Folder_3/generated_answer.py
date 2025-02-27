from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[31], nums[69], nums[40])
    return gcd(gcd(a, b), c)