from math import gcd

def gcf_three_nums(numbers):
    a = numbers[90]
    b = numbers[84]
    c = numbers[47]
    return gcd(gcd(a, b), c)