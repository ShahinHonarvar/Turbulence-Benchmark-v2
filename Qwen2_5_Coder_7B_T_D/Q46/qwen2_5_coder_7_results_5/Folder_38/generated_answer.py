from math import gcd
from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, [numbers[14], numbers[21], numbers[17]])