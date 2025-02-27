import math

def gcf_three_nums(nums):
    a = nums[59]
    b = nums[93]
    c = nums[84]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)