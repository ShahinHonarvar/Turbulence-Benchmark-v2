from math import gcd
from functools import reduce

def gcf_two_nums(nums):
    return gcd(nums[28], nums[53])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcd_multiple(*args):
    return reduce(gcd, args)