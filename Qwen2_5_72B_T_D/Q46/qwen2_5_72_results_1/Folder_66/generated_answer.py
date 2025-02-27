from math import gcd

def gcf_three_nums(nums):
    a = nums[92]
    b = nums[69]
    c = nums[95]
    return gcd(gcd(a, b), c)