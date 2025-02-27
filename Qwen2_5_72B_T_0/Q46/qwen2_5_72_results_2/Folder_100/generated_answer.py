from math import gcd

def gcf_three_nums(numbers):
    a = numbers[21]
    b = numbers[51]
    c = numbers[33]
    return gcd(gcd(a, b), c)