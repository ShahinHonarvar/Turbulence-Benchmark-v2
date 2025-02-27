from math import gcd

def gcf_three_nums(lst):
    a = lst[13]
    b = lst[46]
    c = lst[49]
    return gcd(gcd(a, b), c)