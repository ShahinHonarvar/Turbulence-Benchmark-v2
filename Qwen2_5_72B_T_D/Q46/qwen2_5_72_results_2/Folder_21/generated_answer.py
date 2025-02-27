from math import gcd

def gcf_three_nums(lst):
    a = lst[412]
    b = lst[932]
    c = lst[337]
    return gcd(gcd(a, b), c)