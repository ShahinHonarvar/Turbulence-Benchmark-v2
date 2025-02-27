from math import gcd

def gcf_three_nums(nums):
    num1 = nums[23]
    num2 = nums[46]
    num3 = nums[84]
    result = gcd(gcd(num1, num2), num3)
    return result