from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[15], nums[51], nums[76])
    return gcd(gcd(a, b), c)