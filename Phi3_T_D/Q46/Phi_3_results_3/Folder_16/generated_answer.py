from math import gcd

def gcf_three_nums(lst):
    num1 = lst[558 % len(lst)]
    num2 = lst[110 % len(lst)]
    num3 = lst[628 % len(lst)]
    return gcd(gcd(num1, num2), num3)