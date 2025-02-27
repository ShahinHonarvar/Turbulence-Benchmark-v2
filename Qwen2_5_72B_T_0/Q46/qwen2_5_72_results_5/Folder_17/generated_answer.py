from math import gcd

def gcf_three_nums(numbers):
    a = numbers[20]
    b = numbers[51]
    c = numbers[62]
    return gcd(gcd(a, b), c)