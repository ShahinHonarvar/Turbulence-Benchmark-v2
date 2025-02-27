from math import gcd

def gcf_three_nums(numbers):
    a = numbers[76]
    b = numbers[35]
    c = numbers[74]
    return gcd(gcd(a, b), c)