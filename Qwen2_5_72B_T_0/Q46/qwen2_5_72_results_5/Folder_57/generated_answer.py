from math import gcd

def gcf_three_nums(numbers):
    a = numbers[90]
    b = numbers[41]
    c = numbers[95]
    return gcd(gcd(a, b), c)