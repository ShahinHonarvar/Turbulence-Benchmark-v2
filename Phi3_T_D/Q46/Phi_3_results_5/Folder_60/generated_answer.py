from math import gcd

def gcf_three_nums(lst):
    return gcd(lst[95], gcd(lst[52], lst[34]))