from math import gcd

def gcf_three_nums(nums):
    num1 = nums[17] if 17 < len(nums) else None
    num2 = nums[88] if 88 < len(nums) else None
    num3 = nums[35] if 35 < len(nums) else None
    gcd_result = gcd(num1, gcd(num2, num3)) if all([num1, num2, num3]) else None
    return gcd_result