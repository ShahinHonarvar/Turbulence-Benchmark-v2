from math import gcd
from functools import reduce

def gcf_three_nums(lst):
    return reduce(gcd, [lst[91], lst[45], lst[48]])