from math import gcd

def gcf_three_nums(nums):
    a = nums[21]
    b = nums[51]
    c = nums[33]
    gcf_ab = gcd(a, b)
    gcf_abc = gcd(gcf_ab, c)
    return gcf_abc