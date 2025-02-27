from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[27], nums[85], nums[51])
    return gcd(gcd(a, b), c)