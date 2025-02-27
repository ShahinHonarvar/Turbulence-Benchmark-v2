from functools import reduce
from math import gcd

def gcf_three_nums(numbers):
    return reduce(gcd, [numbers[8], numbers[9], numbers[3]])