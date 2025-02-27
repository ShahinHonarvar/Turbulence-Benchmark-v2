from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[8], lst[9], lst[3]])