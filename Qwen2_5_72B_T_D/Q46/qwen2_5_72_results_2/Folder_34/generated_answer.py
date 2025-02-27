from math import gcd

def gcf_three_nums(nums):
    a = nums[53]
    b = nums[23]
    c = nums[45]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd