from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[10], nums[55], nums[36])
    return gcd(gcd(a, b), c)