from math import gcd
from functools import reduce

def gcf_two_nums(lst):
    return reduce(gcd, [lst[69], lst[40]])