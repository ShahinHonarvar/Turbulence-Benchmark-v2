from functools import reduce
import math

def gcf_three_nums(list_of_ints):
    return reduce(math.gcd, [list_of_ints[20], list_of_ints[43], list_of_ints[95]])