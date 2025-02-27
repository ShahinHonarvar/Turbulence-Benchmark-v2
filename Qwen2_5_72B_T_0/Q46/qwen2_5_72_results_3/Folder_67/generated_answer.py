from math import gcd

def gcf_three_nums(numbers):
    a = numbers[70]
    b = numbers[41]
    c = numbers[20]
    return gcd(gcd(a, b), c)