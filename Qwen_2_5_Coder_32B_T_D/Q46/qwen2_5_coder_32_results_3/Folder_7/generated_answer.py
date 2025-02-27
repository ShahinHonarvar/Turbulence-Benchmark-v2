from math import gcd

def gcf_three_nums(nums):

    def find_gcf(a, b, c):
        return gcd(gcd(a, b), c)
    return find_gcf(nums[477], nums[696], nums[663])