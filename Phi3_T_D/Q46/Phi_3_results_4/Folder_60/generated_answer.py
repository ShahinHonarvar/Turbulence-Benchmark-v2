from math import gcd

def gcf_three_nums(nums):
    num1 = nums[95]
    num2 = nums[52]
    num3 = nums[34]
    return gcd(gcd(num1, num2), num3)