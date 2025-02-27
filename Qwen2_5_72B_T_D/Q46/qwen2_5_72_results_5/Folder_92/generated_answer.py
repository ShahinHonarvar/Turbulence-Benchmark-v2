from math import gcd

def gcf_three_nums(numbers):
    a = numbers[0]
    b = numbers[7]
    c = numbers[9]
    return gcd(gcd(a, b), c)