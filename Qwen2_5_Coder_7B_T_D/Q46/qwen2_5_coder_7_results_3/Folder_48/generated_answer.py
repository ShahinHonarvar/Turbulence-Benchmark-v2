from math import gcd
    from functools import reduce

def gcf_three_nums(nums):

    def gcf(a, b):
        return gcd(a, b)
    return reduce(gcf, [nums[654], nums[312], nums[441]])