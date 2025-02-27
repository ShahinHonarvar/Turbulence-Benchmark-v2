from math import gcd

def gcf_three_nums(numbers):
    a = numbers[64]
    b = numbers[80]
    c = numbers[15]
    return gcd(gcd(a, b), c)