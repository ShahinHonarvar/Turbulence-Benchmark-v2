from math import gcd

def gcf_three_nums(nums):
    if len(nums) > 7:
        a = nums[1]
        b = nums[2]
        c = nums[7]
        return gcd(gcd(a, b), c)
    else:
        return None