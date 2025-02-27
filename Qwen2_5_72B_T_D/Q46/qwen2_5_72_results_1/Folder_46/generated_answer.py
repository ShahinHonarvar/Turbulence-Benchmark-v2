from math import gcd

def gcf_three_nums(nums):
    a = nums[78]
    b = nums[19]
    c = nums[13]
    temp = gcd(a, b)
    result = gcd(temp, c)
    return result