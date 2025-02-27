from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[25], nums[76], nums[57])
    return gcd(gcd(a, b), c)