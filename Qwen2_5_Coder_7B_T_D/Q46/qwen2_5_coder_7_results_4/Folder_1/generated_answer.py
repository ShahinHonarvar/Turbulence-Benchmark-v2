from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[74], lst[51], lst[27]])