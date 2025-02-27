import math

def gcf_three_nums(nums):
    num1 = nums[412]
    num2 = nums[932]
    num3 = nums[337]
    gcf = math.gcd(num1, num2)
    gcf = math.gcd(gcf, num3)
    return gcf