from math import gcd

def gcf_three_nums(numbers):
    a = numbers[23]
    b = numbers[46]
    c = numbers[84]
    return gcd(gcd(a, b), c)