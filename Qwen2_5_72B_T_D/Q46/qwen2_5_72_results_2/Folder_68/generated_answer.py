from math import gcd

def gcf_three_nums(nums):
    a = nums[4]
    b = nums[1]
    c = nums[7]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd