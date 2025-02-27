import math

def gcf_three_nums(nums):
    a = nums[86]
    b = nums[89]
    c = nums[49]
    return math.gcd(math.gcd(a, b), c)