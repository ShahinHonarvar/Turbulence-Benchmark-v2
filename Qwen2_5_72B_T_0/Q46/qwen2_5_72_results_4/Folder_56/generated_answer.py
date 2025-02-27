from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[59], nums[93], nums[84])
    return gcd(gcd(a, b), c)