from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[93], nums[94], nums[57])
    return gcd(gcd(a, b), c)