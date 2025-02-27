from math import gcd

def gcf_three_nums(numbers):
    a = numbers[37]
    b = numbers[30]
    c = numbers[48]
    return gcd(gcd(a, b), c)