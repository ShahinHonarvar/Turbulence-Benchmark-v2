from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[27], lst[51], lst[74])
    return gcd(gcd(a, b), c)