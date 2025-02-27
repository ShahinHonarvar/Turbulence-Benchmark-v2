from math import gcd

def gcf_three_nums(nums):
    a = nums[10]
    b = nums[55]
    c = nums[36]
    return gcd(gcd(a, b), c)