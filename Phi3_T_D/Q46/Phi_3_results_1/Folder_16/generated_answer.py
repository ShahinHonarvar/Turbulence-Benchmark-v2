from math import gcd

def gcf_three_nums(nums):
    a, b, c = (nums[558], nums[110], nums[628])
    return gcd(gcd(a, b), c)