from math import gcd

def gcf_three_nums(numbers):
    a = numbers[44]
    b = numbers[91]
    c = numbers[42]
    return gcd(gcd(a, b), c)