from math import gcd

def gcf_three_nums(numbers):
    a = numbers[25]
    b = numbers[76]
    c = numbers[57]
    return gcd(gcd(a, b), c)