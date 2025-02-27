import math

def gcf_two_nums(lst):
    if len(lst) < max(43, 99):
        return None
    return math.gcd(lst[42], lst[98])