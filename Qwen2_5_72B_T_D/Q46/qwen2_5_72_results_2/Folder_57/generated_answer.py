from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[90], lst[41], lst[95])
    return gcd(gcd(a, b), c)