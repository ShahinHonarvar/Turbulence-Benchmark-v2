from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, [numbers[41], numbers[69], numbers[28]])