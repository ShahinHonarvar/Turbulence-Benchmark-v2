from math import gcd
    import functools

def gcf_three_nums(lst):
    return functools.reduce(gcd, [lst[41], lst[69], lst[28]])