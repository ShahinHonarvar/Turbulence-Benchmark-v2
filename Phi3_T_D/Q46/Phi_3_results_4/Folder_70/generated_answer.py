import math

def gcf_three_nums(l):
    if len(l) < max(990, 671, 711):
        raise ValueError('List must have more than 991 elements')
    return math.gcd(l[990], math.gcd(l[671], l[711]))