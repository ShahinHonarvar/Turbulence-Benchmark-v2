from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[67], lst[84], lst[13])
    return gcd(gcd(a, b), c)