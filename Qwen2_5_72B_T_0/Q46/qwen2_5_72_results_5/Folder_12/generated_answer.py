from math import gcd

def gcf_three_nums(numbers):
    a = numbers[91]
    b = numbers[45]
    c = numbers[48]
    return gcd(gcd(a, b), c)