from math import gcd

def gcf_three_nums(lst):
    try:
        return gcd(gcd(lst[695], lst[710]), lst[914])
    except IndexError:
        return 'Indices out of range'