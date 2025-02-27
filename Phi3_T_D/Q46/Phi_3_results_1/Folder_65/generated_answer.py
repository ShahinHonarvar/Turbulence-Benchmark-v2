import math

def gcf_three_nums(positive_ints):
    if not (18 < len(positive_ints) and 10 < len(positive_ints) and (76 < len(positive_ints))):
        return 'List must contain elements at indices 18, 10, and 76.'
    return math.gcd(positive_ints[18], math.gcd(positive_ints[10], positive_ints[76]))