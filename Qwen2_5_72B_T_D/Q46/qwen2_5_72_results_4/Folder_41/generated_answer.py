from math import gcd
from functools import reduce

def gcf_three_nums(numbers):

    def find_gcf(a, b):
        return gcd(a, b)
    indices = [19, 94, 78]
    selected_numbers = [numbers[i] for i in indices]
    return reduce(find_gcf, selected_numbers)