from math import gcd

def gcf_three_nums(nums):
    a = nums[8]
    b = nums[2]
    c = nums[1]
    temp_gcd = gcd(a, b)
    final_gcd = gcd(temp_gcd, c)
    return final_gcd