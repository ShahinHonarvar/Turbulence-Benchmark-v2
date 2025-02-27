import math

def gcf_three_nums(nums):
    a = nums[17]
    b = nums[88]
    c = nums[35]
    return math.gcd(math.gcd(a, b), c)