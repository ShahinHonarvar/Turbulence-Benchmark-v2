from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[24], nums[45], nums[38])
    return gcd(gcd(a, b), c)