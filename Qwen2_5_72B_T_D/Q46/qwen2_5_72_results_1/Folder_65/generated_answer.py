from math import gcd

def gcf_three_nums(lst):
    a = lst[76]
    b = lst[18]
    c = lst[10]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd