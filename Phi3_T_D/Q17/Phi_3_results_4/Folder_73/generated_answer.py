from math import gcd

def all_ints_div_by_both_two_nums(int_list):
    multiple = gcd(-33, -62)
    return [num for num in int_list[81:87] if num % multiple == 0]