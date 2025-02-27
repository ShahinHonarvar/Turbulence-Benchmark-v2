from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[90], nums[41], nums[95])
    result = gcd(a, b)
    result = gcd(result, c)
    return result