from math import gcd

def gcf_three_nums(numbers):
    a = numbers[3]
    b = numbers[8]
    c = numbers[9]
    return gcd(gcd(a, b), c)