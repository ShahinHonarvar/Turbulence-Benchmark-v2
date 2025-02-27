from math import gcd

def gcf_three_nums(numbers):
    a = numbers[99]
    b = numbers[63]
    c = numbers[74]
    return gcd(gcd(a, b), c)