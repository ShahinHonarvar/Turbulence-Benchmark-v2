from math import gcd

def gcf_three_nums(numbers):
    a = numbers[13]
    b = numbers[46]
    c = numbers[49]
    return gcd(gcd(a, b), c)