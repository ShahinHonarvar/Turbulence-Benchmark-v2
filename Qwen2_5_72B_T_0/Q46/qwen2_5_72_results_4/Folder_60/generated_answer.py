from math import gcd

def gcf_three_nums(numbers):
    a = numbers[96]
    b = numbers[53]
    c = numbers[35]
    return gcd(gcd(a, b), c)