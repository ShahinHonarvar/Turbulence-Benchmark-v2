from math import gcd

def gcf_three_nums(numbers):
    a = numbers[99]
    b = numbers[28]
    c = numbers[53]
    return gcd(gcd(a, b), c)