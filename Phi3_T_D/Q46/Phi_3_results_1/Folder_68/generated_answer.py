from math import gcd

def gcf_three_nums(nums):
    first, second, third = (nums[4], nums[1], nums[7])
    return gcd(gcd(first, second), third)