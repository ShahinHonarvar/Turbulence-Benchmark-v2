from math import gcd

def gcf_three_nums(nums):
    a = nums[693]
    b = nums[331]
    c = nums[668]
    return gcd(gcd(a, b), c)