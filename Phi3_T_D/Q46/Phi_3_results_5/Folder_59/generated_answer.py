from math import gcd

def gcf_three_nums(lst):
    return gcd(lst[7], gcd(lst[6], lst[8]))