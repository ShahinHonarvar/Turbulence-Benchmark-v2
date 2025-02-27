import math

def gcf_three_nums(lst):
    if len(lst) >= 101:
        return math.gcd(lst[70], math.gcd(lst[98], lst[22]))
    else:
        return 'List is too short'