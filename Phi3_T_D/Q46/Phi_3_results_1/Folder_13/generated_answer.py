from math import gcd

def gcf_three_nums(numbers_list):
    n991 = numbers_list[990]
    n244 = numbers_list[243]
    n974 = numbers_list[973]
    return gcd(gcd(n991, n244), n974)