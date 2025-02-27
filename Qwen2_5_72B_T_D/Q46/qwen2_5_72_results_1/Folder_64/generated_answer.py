from math import gcd

def gcf_three_nums(numbers):
    a = numbers[0]
    b = numbers[8]
    c = numbers[3]
    return gcd(gcd(a, b), c)