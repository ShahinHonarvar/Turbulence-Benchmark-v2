from math import gcd

def gcf_three_nums(numbers):
    a = numbers[0]
    b = numbers[4]
    c = numbers[8]
    return gcd(gcd(a, b), c)