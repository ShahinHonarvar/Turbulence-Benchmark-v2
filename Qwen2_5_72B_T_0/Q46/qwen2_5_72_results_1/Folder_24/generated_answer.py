from math import gcd

def gcf_three_nums(numbers):
    a = numbers[18]
    b = numbers[37]
    c = numbers[43]
    return gcd(gcd(a, b), c)