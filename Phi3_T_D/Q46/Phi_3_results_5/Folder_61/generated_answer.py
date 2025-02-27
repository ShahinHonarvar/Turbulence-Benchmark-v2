from math import gcd

def gcf_three_nums(lst):
    return gcd(lst[1], gcd(lst[2], lst[7]))