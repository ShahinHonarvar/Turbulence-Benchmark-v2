from math import gcd

def gcf_three_nums(nums):
    a = nums[307]
    b = nums[920]
    c = nums[463]
    return gcd(gcd(a, b), c)