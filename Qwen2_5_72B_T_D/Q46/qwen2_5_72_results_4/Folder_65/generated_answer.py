from math import gcd

def gcf_three_nums(numbers):
    a = numbers[76]
    b = numbers[18]
    c = numbers[10]
    return gcd(gcd(a, b), c)