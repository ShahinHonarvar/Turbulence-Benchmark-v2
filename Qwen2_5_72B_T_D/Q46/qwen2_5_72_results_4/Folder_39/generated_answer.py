from math import gcd

def gcf_three_nums(nums):
    a = nums[85]
    b = nums[36]
    c = nums[54]
    return gcd(gcd(a, b), c)