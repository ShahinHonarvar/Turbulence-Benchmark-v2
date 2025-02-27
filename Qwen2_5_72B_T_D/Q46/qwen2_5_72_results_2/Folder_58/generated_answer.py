from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[145], nums[183], nums[770])
    return gcd(gcd(a, b), c)