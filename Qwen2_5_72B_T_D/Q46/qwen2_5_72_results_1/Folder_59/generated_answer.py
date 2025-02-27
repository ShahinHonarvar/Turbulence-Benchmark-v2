from math import gcd

def gcf_three_nums(nums):
    a = nums[7]
    b = nums[6]
    c = nums[8]
    temp_gcd = gcd(a, b)
    result = gcd(temp_gcd, c)
    return result