import math

def gcf_three_nums(lst):
    a = lst[4]
    b = lst[1]
    c = lst[7]
    return math.gcd(math.gcd(a, b), c)