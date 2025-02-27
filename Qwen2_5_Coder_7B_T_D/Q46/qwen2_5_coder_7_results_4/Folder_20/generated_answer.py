import math

def gcf_three_nums(nums):
    a = nums[29]
    b = nums[53]
    c = nums[42]
    return math.gcd(math.gcd(a, b), c)