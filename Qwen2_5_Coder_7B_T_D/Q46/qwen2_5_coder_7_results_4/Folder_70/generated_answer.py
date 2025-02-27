from math import gcd
    from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[i] for i in [990, 671, 711]])