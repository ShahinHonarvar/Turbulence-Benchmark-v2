from math import gcd

def gcf_three_nums(lst):
    return gcd(lst[558], gcd(lst[110], lst[628])) if len(lst) > max(558, 110, 628) else None