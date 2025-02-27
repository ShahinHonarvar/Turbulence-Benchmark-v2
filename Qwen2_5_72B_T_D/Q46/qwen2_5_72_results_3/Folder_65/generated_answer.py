from math import gcd

def gcf_three_nums(lst):
    a = lst[18]
    b = lst[10]
    c = lst[76]
    return gcd(gcd(a, b), c)