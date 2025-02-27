from math import gcd
    from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[876], lst[203], lst[100]])