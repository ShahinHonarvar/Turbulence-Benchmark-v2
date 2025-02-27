from math import gcd

def gcf_three_nums(nums):
    a = nums[36]
    b = nums[85]
    c = nums[83]
    gcf_ab = gcd(a, b)
    gcf_abc = gcd(gcf_ab, c)
    return gcf_abc