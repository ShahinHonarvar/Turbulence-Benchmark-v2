from math import gcd

def gcf_three_nums(numbers):
    a = numbers[412]
    b = numbers[932]
    c = numbers[337]
    return gcd(gcd(a, b), c)