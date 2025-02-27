from math import gcd

def gcf_three_nums(nums):
    a = nums[944]
    b = nums[814]
    c = nums[865]
    return gcd(gcd(a, b), c)