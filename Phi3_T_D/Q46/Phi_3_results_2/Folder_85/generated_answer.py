from math import gcd

def gcf_three_nums(lst):
    a = lst[48]
    b = lst[45]
    c = lst[12]
    return gcd(gcd(a, b), c)