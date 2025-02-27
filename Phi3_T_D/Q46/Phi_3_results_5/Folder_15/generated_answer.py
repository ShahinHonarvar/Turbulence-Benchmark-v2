from math import gcd

def gcf_three_nums(li):
    a, b, c = (li[4], li[0], li[8])
    return gcd(gcd(a, b), c)