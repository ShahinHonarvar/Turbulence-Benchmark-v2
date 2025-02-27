import math

def gcf_three_nums(lst):
    a = lst[59]
    b = lst[93]
    c = lst[84]
    return math.gcd(math.gcd(a, b), c)