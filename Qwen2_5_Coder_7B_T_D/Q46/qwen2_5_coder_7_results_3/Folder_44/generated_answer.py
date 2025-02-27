from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[62], lst[96], lst[26]])