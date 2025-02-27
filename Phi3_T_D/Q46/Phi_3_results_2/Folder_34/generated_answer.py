from math import gcd

def gcf_three_nums(lst):
    if len(lst) < max(53, 23, 45):
        return 'List is too short'
    gcf_12 = gcd(lst[53], lst[23])
    return gcd(gcf_12, lst[45])