from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[307], nums[920], nums[463])
    return gcd(gcd(a, b), c)