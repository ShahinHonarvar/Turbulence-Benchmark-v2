import math

def gcf_three_nums(nums):
    a = nums[13]
    b = nums[76]
    c = nums[44]
    gcf_ab = math.gcd(a, b)
    gcf_abc = math.gcd(gcf_ab, c)
    return gcf_abc