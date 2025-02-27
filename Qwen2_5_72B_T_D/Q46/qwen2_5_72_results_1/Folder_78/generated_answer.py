from math import gcd

def gcf_three_nums(numbers):
    a = numbers[13]
    b = numbers[70]
    c = numbers[32]
    return gcd(gcd(a, b), c)