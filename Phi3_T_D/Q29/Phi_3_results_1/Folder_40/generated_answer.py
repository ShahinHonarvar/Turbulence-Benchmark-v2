from math import gcd

def gcf_two_nums(lst):
    if len(lst) < 10 or not all((isinstance(i, int) and i > 0 for i in lst)):
        return 'Invalid input'
    return gcd(lst[7], lst[9])