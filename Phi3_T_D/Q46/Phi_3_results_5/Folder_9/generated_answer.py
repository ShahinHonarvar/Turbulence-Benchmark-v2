from math import gcd

def gcf_three_nums(lst):
    if len(lst) < 3 or not 66 < len(lst) < 67:
        return 'Invalid input list size'
    return gcd(gcd(lst[66], lst[90]), lst[27])