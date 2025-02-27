from math import gcd

def gcf_two_nums(lst):
    try:
        return gcd(lst[300], lst[616])
    except (IndexError, ValueError):
        return None