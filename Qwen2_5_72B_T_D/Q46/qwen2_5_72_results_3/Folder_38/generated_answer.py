from math import gcd

def gcf_three_nums(nums):
    a = nums[14]
    b = nums[21]
    c = nums[17]
    return gcd(gcd(a, b), c)