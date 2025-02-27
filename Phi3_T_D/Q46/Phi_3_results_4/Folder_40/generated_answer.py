from math import gcd

def gcf_three_nums(int_list):
    return gcd(int_list[1], gcd(int_list[6], int_list[8]))