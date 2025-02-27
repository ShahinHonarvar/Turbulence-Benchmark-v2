import math

def gcf_three_nums(nums):
    num1 = nums[991]
    num2 = nums[244]
    num3 = nums[974]
    gcf = math.gcd(num1, num2)
    gcf = math.gcd(gcf, num3)
    return gcf