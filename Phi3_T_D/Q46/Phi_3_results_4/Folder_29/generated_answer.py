import math

def gcf_three_nums(lst):
    return math.gcd(lst[22], math.gcd(lst[97], lst[64])) if len(lst) > max(22, 97, 64) else None