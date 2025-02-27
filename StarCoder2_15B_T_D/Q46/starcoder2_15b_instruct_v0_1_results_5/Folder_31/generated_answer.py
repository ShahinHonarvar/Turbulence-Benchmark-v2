from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[90], nums[54], nums[96])
    return gcd(a, gcd(b, c))