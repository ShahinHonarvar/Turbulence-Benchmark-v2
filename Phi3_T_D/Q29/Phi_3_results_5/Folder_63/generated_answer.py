import math

def gcf_two_nums(lst):
    if len(lst) > 21 and len(lst) > 17:
        return math.gcd(lst[21], lst[17])
    else:
        return None