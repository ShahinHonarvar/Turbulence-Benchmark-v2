import math

def gcf_three_nums(lst):
    a = lst[23]
    b = lst[46]
    c = lst[84]
    x = math.gcd(a, b)
    y = math.gcd(x, c)
    return y