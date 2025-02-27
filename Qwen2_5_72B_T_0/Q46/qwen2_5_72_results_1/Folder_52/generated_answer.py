from math import gcd

def gcf_three_nums(numbers):
    a = numbers[19]
    b = numbers[49]
    c = numbers[74]
    return gcd(gcd(a, b), c)