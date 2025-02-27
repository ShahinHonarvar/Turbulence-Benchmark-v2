from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[64], lst[80], lst[15]])