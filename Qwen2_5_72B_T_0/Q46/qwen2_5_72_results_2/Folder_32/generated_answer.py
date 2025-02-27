from math import gcd

def gcf_three_nums(numbers):
    a = numbers[20]
    b = numbers[43]
    c = numbers[95]
    return gcd(gcd(a, b), c)