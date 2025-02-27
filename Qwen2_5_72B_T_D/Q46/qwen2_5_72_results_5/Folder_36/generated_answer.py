from math import gcd

def gcf_three_nums(nums):
    a = nums[427]
    b = nums[761]
    c = nums[148]
    return gcd(gcd(a, b), c)