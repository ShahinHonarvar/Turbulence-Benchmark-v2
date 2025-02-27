from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[66], nums[56], nums[92])
    return gcd(gcd(a, b), c)