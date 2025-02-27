from math import gcd

def gcf_three_nums(nums):
    a = nums[87]
    b = nums[20]
    c = nums[36]
    temp_gcd = gcd(a, b)
    final_gcd = gcd(temp_gcd, c)
    return final_gcd