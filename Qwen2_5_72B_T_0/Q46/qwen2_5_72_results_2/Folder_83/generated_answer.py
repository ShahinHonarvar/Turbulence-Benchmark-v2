from math import gcd

def gcf_three_nums(numbers):
    a = numbers[56]
    b = numbers[54]
    c = numbers[13]
    return gcd(gcd(a, b), c)