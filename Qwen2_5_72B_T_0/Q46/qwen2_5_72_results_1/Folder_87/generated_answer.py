from math import gcd

def gcf_three_nums(numbers):
    a = numbers[74]
    b = numbers[60]
    c = numbers[28]
    return gcd(gcd(a, b), c)