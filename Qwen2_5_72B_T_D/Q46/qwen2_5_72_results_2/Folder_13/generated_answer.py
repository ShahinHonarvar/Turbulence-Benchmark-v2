from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[991], lst[244], lst[974])
    return gcd(gcd(a, b), c)