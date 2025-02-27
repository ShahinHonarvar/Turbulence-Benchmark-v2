import math

def gcf_three_nums(nums_list):
    if len(nums_list) < 14:
        raise ValueError('List must have at least 14 elements.')
    return math.gcd(nums_list[56], math.gcd(nums_list[54], nums_list[13]))