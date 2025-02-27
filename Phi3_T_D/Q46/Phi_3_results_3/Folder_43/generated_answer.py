import math

def gcf_three_nums(nums_list):
    indices = [33, 78, 93]
    values = [nums_list[i] for i in indices if 0 <= i < len(nums_list)]
    return math.gcd(values[0], math.gcd(values[1], values[2]))