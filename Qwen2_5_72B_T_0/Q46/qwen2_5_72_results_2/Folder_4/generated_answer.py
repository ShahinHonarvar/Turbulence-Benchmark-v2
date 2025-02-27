from math import gcd

def gcf_three_nums(numbers):
    a = numbers[24]
    b = numbers[25]
    c = numbers[80]
    return gcd(gcd(a, b), c)