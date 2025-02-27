from math import gcd

def gcf_three_nums(nums):
    a = nums[53]
    b = nums[23]
    c = nums[45]
    x = gcd(a, b)
    y = gcd(x, c)
    return y