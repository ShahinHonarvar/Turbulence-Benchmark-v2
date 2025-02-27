from math import gcd

def gcf_three_nums(numbers):
    a = numbers[41]
    b = numbers[69]
    c = numbers[28]
    return gcd(gcd(a, b), c)