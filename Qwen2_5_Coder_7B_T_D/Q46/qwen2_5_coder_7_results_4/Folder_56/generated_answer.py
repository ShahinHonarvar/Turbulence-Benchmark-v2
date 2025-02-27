from math import gcd
    from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, [numbers[59], numbers[93], numbers[84]])