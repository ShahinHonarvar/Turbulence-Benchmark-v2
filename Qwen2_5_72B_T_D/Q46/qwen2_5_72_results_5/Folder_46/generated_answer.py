from math import gcd

def gcf_three_nums(nums):
    a = nums[78]
    b = nums[19]
    c = nums[13]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd