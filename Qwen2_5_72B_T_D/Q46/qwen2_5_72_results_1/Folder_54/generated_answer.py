from math import gcd

def gcf_three_nums(numbers):
    a = numbers[96]
    b = numbers[57]
    c = numbers[85]
    return gcd(gcd(a, b), c)