from math import gcd

def gcf_three_nums(numbers):
    a = numbers[99]
    b = numbers[95]
    c = numbers[80]
    return gcd(gcd(a, b), c)