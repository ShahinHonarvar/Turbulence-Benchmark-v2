from math import gcd

def gcf_three_nums(nums):

    def gcf(x, y, z):
        return gcd(gcd(x, y), z)
    return gcf(nums[29], nums[74], nums[49])