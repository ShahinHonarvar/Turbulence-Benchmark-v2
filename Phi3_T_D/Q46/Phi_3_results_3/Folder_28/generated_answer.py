from math import gcd

def gcf_three_nums(lst):
    return gcd(lst[99], gcd(lst[63], lst[74]))