from math import gcd

def gcf_three_nums(numbers):
    a = numbers[47]
    b = numbers[10]
    c = numbers[28]
    return gcd(gcd(a, b), c)