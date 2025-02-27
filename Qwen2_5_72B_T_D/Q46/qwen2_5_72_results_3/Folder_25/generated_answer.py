from math import gcd

def gcf_three_nums(lst):
    a = lst[32]
    b = lst[54]
    c = lst[13]
    return gcd(gcd(a, b), c)