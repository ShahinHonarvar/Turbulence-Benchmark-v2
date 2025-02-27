from math import gcd

def gcf_three_nums(numbers):
    a = numbers[17]
    b = numbers[88]
    c = numbers[35]
    return gcd(gcd(a, b), c)