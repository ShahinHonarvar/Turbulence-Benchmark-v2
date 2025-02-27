import math

def gcf_three_nums(lst):
    if len(lst) < 8 or not all((isinstance(x, int) and x > 0 for x in lst)):
        raise ValueError('List must contain at least 8 positive integers.')
    return math.gcd(lst[7], math.gcd(lst[6], lst[8]))