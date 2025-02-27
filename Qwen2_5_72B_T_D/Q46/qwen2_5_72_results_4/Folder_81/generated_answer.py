from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[20], lst[17], lst[28])
    return gcd(gcd(a, b), c)