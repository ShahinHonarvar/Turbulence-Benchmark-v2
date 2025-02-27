from math import gcd

def gcf_three_nums(lst):
    if len(lst) < max(90, 84, 47):
        raise ValueError('List is too short.')
    return gcd(gcd(lst[90], lst[84]), lst[47])