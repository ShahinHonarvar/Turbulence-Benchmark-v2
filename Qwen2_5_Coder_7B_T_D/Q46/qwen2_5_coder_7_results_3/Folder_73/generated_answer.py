from math import gcd
    from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, (numbers[90], numbers[84], numbers[47]))