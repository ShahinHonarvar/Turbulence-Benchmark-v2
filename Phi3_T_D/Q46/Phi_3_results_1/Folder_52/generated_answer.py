from math import gcd

def gcf_three_nums(nums):
    try:
        a, b, c = (nums[18], nums[48], nums[73])
        return gcd(gcd(a, b), c)
    except IndexError:
        raise ValueError('List must have at least 74 elements.')