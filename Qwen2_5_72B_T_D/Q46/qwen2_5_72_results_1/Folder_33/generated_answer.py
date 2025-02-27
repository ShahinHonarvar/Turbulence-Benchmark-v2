from math import gcd

def gcf_three_nums(lst):
    if len(lst) <= 564:
        return None
    return gcd(gcd(lst[252], lst[149]), lst[564])