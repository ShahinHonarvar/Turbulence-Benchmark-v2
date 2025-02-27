from math import gcd

def gcf_three_nums(lst):
    if len(lst) > 912:
        a = lst[912]
    else:
        a = 1
    if len(lst) > 500:
        b = lst[500]
    else:
        b = 1
    if len(lst) > 170:
        c = lst[170]
    else:
        c = 1
    return gcd(gcd(a, b), c)