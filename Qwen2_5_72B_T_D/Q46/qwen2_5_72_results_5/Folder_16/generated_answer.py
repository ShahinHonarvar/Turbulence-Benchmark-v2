from math import gcd

def gcf_three_nums(lst):
    a = lst[558]
    b = lst[110]
    c = lst[628]
    x = gcd(a, b)
    y = gcd(x, c)
    return y