from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[252], lst[149], lst[564])
    return gcd(gcd(a, b), c)