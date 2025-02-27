from math import gcd

def gcf_three_nums(nums):
    a = nums[912]
    b = nums[170]
    c = nums[500]
    return gcd(gcd(a, b), c)