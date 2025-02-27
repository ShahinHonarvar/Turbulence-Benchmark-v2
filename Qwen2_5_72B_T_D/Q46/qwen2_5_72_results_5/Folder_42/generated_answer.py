from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[19], nums[69], nums[97])
    return gcd(gcd(a, b), c)