from math import gcd

def gcf_three_nums(lst):
    a = lst[37]
    b = lst[30]
    c = lst[48]
    return gcd(gcd(a, b), c)