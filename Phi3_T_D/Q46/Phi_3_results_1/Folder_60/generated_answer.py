import math

def gcf_three_nums(nums):
    index96, index53, index35 = (nums[95], nums[52], nums[34])
    return math.gcd(math.gcd(index96, index53), index35)