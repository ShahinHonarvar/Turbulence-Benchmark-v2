from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[91], nums[45], nums[48])
    return gcd(gcd(a, b), c)