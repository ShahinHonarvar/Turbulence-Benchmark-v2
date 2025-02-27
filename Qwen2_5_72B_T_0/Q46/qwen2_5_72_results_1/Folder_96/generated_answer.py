from math import gcd

def gcf_three_nums(numbers):
    a = numbers[29]
    b = numbers[74]
    c = numbers[49]
    return gcd(gcd(a, b), c)