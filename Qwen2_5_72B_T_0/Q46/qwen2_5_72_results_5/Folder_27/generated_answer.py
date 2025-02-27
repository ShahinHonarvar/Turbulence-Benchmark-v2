from math import gcd

def gcf_three_nums(numbers):
    a = numbers[76]
    b = numbers[64]
    c = numbers[28]
    return gcd(gcd(a, b), c)