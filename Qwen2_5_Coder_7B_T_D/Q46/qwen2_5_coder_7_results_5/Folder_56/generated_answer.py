from math import gcd

def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(nums[59], nums[93]), nums[84])