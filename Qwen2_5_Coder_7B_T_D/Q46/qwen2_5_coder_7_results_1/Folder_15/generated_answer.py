from math import gcd
    from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[4], lst[0], lst[8]])