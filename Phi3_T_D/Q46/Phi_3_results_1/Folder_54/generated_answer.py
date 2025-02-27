from math import gcd

def gcf_three_nums(lst):
    x, y, z = (lst[96], lst[57], lst[85])
    return gcd(gcd(x, y), z)