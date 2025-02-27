from math import gcd

def gcf_three_nums(lst):
    nums = [lst[78], lst[19], lst[13]]
    return gcd(gcd(nums[0], nums[1]), nums[2])