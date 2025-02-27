from math import gcd

def gcf_three_nums(numbers):
    a = numbers[40]
    b = numbers[15]
    c = numbers[99]
    return gcd(gcd(a, b), c)