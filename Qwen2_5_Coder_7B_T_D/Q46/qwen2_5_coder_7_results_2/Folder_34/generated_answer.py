from math import gcd
from functools import reduce

def gcf_three_nums(num_list):
    return reduce(gcd, [num_list[53], num_list[23], num_list[45]])