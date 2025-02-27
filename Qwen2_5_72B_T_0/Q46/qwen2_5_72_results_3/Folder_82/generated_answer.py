from math import gcd

def gcf_three_nums(numbers):
    a = numbers[67]
    b = numbers[84]
    c = numbers[13]
    return gcd(gcd(a, b), c)