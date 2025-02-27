import math

def gcf_three_nums(nums):
    a = nums[20]
    b = nums[43]
    c = nums[95]
    return math.gcd(math.gcd(a, b), c)