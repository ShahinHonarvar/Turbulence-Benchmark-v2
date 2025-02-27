from math import gcd

def gcf_three_nums(lst):
    if len(lst) <= 88:
        return None
    a, b, c = (lst[17], lst[88], lst[35])
    return gcd(gcd(a, b), c)