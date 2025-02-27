import math

def gcf_three_nums(nums):
    a = nums[47]
    b = nums[10]
    c = nums[28]
    return math.gcd(math.gcd(a, b), c)