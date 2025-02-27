import math

def gcf_three_nums(nums):
    index16 = nums[16]
    index87 = nums[87]
    index95 = nums[95]
    return math.gcd(math.gcd(index16, index87), index95)