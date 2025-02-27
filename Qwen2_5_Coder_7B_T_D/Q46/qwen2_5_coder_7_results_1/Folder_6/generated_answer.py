import math

def gcf_three_nums(nums):
    a = nums[93]
    b = nums[94]
    c = nums[57]
    return math.gcd(math.gcd(a, b), c)