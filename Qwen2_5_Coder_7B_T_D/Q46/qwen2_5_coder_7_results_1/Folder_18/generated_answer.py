from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[637], lst[411], lst[757]])