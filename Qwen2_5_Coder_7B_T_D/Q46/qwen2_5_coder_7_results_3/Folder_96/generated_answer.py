from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, [numbers[29], numbers[74], numbers[49]])