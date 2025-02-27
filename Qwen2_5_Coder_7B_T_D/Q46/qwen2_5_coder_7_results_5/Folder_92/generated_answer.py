from math import gcd
    from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, [numbers[7], numbers[9], numbers[0]])