from math import gcd

def gcf_three_nums(nums):

    def three_gcd(a, b, c):
        return gcd(gcd(a, b), c)
    return three_gcd(nums[53], nums[23], nums[45])