from math import gcd

def gcf_three_nums(lst):
    return gcd(lst[742], gcd(lst[888], lst[629])) if len(lst) > max(742, 888, 629) else None