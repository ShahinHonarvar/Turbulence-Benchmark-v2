from math import gcd
    from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, [numbers[33], numbers[78], numbers[93]])