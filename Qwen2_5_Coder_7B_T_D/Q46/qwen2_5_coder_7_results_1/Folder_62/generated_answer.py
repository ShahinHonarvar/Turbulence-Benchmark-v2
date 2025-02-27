from math import gcd

def gcf_three_nums(nums):

    def gcf(a, b):
        return gcd(a, gcd(b, nums[36]))
    return gcf(nums[10], nums[55])