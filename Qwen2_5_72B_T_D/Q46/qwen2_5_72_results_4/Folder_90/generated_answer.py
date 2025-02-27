from math import gcd

def gcf_three_nums(nums):
    a = nums[818]
    b = nums[606]
    c = nums[873]
    return gcd(gcd(a, b), c)