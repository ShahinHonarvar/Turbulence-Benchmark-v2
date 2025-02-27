from math import gcd

def gcf_three_nums(lst):
    a = lst[7]
    b = lst[6]
    c = lst[8]
    return gcd(gcd(a, b), c)