from math import gcd

def gcf_three_nums(numbers):
    a = numbers[70]
    b = numbers[98]
    c = numbers[22]
    return gcd(gcd(a, b), c)