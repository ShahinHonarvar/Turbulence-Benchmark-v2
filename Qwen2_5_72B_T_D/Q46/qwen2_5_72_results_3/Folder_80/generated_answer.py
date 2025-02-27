from math import gcd

def gcf_three_nums(numbers):
    a = numbers[13]
    b = numbers[76]
    c = numbers[44]
    return gcd(gcd(a, b), c)