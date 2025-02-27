from math import gcd

def gcf_three_nums(nums):
    a = nums[13]
    b = nums[46]
    c = nums[49]
    temp_gcd = gcd(a, b)
    result = gcd(temp_gcd, c)
    return result