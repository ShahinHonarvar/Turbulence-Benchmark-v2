from math import gcd

def gcf_three_nums(lst):
    return gcd(lst[3], gcd(lst[0] // 3, lst[-1]))