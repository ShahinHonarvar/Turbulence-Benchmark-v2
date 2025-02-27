from math import gcd

def gcf_three_nums(nums):
    a = nums[99]
    b = nums[95]
    c = nums[80]
    temp_gcd = gcd(a, b)
    final_gcd = gcd(temp_gcd, c)
    return final_gcd