import math

def gcf_three_nums(nums):
    a = nums[1]
    b = nums[6]
    c = nums[8]
    return math.gcd(math.gcd(a, b), c)