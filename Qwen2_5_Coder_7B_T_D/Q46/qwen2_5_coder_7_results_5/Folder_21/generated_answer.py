import math

def gcf_three_nums(nums):
    a, b, c = (nums[412], nums[932], nums[337])
    return math.gcd(math.gcd(a, b), c)