from math import gcd

def gcf_three_nums(numbers):
    a = numbers[4]
    b = numbers[1]
    c = numbers[7]
    return gcd(gcd(a, b), c)