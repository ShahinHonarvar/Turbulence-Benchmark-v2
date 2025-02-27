from math import gcd

def gcf_three_nums(lst):
    num1 = lst[558]
    num2 = lst[110]
    num3 = lst[628]
    return gcd(gcd(num1, num2), num3)