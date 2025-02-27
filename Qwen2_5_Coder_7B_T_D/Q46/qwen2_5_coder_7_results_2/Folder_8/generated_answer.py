from math import gcd
    from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[99], lst[28], lst[53]])