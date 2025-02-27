from math import gcd

def gcf_three_nums(nums):
    num1 = nums[99]
    num2 = nums[63]
    num3 = nums[74]
    result = gcd(gcd(num1, num2), num3)
    return result