from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[56], nums[88], nums[51])
    return gcd(gcd(a, b), c)