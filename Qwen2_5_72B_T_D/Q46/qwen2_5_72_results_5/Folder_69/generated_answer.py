from math import gcd

def gcf_three_nums(nums):
    a = nums[404]
    b = nums[834]
    c = nums[517]
    return gcd(gcd(a, b), c)