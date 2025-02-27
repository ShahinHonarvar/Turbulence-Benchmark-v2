import math

def gcf_three_nums(nums):
    a = nums[20]
    b = nums[51]
    c = nums[62]
    return math.gcd(math.gcd(a, b), c)