from math import gcd

def gcf_three_nums(nums):
    a = nums[412]
    b = nums[932]
    c = nums[337]
    return gcd(gcd(a, b), c)