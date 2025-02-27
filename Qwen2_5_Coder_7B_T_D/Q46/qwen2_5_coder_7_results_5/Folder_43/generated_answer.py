from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[33], lst[78], lst[93]])