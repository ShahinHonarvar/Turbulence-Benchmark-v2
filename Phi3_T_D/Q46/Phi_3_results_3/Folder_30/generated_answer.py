from math import gcd

def gcf_three_nums(lst):
    return gcd(lst[76] if len(lst) > 76 else 1, gcd(lst[35] if len(lst) > 35 else 1, lst[74] if len(lst) > 74 else 1))