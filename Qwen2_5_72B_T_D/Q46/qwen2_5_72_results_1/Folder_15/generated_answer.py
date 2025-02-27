from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[0], lst[4], lst[8])
    return gcd(gcd(a, b), c)