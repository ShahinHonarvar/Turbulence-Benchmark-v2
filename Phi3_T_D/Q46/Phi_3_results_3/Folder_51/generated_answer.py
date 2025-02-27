import math

def gcf_three_nums(nums):
    a = nums[21]
    b = nums[69]
    c = nums[41]
    return math.gcd(math.gcd(a, b), c)