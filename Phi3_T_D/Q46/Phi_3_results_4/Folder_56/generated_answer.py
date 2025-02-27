from math import gcd

def gcf_three_nums(numbers):
    idx_59 = numbers[59]
    idx_93 = numbers[93]
    idx_84 = numbers[84]
    return gcd(gcd(idx_59, idx_93), idx_84)