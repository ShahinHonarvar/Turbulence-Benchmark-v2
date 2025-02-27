from math import gcd

def gcf_three_nums(numbers):
    a = numbers[20]
    b = numbers[17]
    c = numbers[28]
    return gcd(gcd(a, b), c)