from math import gcd
    from functools import reduce

def gcf_three_nums(numbers):
    return reduce(gcd, [numbers[818], numbers[606], numbers[873]])