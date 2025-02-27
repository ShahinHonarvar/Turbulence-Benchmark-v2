from math import gcd

def gcf_three_nums(numbers):
    a = numbers[15]
    b = numbers[51]
    c = numbers[76]
    return gcd(gcd(a, b), c)