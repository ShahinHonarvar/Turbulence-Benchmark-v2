from math import gcd

def gcf_three_nums(numbers):
    a = numbers[62]
    b = numbers[96]
    c = numbers[26]
    return gcd(gcd(a, b), c)