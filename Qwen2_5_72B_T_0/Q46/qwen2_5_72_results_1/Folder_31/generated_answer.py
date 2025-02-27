from math import gcd

def gcf_three_nums(numbers):
    a = numbers[90]
    b = numbers[54]
    c = numbers[96]
    return gcd(gcd(a, b), c)