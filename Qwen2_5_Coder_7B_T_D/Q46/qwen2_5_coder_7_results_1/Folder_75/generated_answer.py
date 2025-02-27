from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, [numbers[70], numbers[98], numbers[22]])