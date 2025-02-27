from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[19], lst[69], lst[97]])