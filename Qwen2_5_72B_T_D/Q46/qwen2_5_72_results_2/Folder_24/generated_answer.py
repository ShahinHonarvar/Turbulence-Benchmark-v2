from math import gcd
from functools import reduce

def gcf_three_nums(numbers):

    def find_gcf(a, b):
        return gcd(a, b)
    specific_numbers = [numbers[18], numbers[37], numbers[43]]
    return reduce(find_gcf, specific_numbers)