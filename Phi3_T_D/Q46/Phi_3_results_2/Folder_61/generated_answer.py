import math

def gcf_three_nums(nums):
    index1 = nums[1]
    index2 = nums[2]
    index7 = nums[7]
    return math.gcd(math.gcd(index1, index2), index7)