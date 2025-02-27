from math import gcd

def gcf_three_nums(lst):
    a, b, c = (lst[62], lst[96], lst[26])
    return gcd(gcd(a, b), c)