from math import gcd

def gcf_three_nums(nums):
    a = nums[87]
    b = nums[20]
    c = nums[36]
    return gcd(gcd(a, b), c)