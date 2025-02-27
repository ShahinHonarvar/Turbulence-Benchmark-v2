from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[37], nums[30], nums[48])
    return gcd(gcd(a, b), c)