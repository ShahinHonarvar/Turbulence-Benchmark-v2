from math import gcd

def gcf_three_nums(nums):
    a = nums[40]
    b = nums[15]
    c = nums[99]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd