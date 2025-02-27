from math import gcd

def gcf_three_nums(numbers):
    a = numbers[22]
    b = numbers[97]
    c = numbers[64]
    return gcd(gcd(a, b), c)