from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[90], nums[41], nums[95])
    return gcd(gcd(a, b), c)