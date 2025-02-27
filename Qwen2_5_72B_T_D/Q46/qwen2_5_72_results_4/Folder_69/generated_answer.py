from math import gcd

def gcf_three_nums(lst):
    num1 = lst[404]
    num2 = lst[834]
    num3 = lst[517]
    result = gcd(gcd(num1, num2), num3)
    return result