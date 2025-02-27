from math import gcd

def gcf_three_nums(lst):
    num1 = lst[8]
    num2 = lst[9]
    num3 = lst[3]
    return gcd(gcd(num1, num2), num3)