from math import gcd

def gcf_three_nums(numbers):
    a = numbers[2]
    b = numbers[6]
    c = numbers[9]
    return gcd(gcd(a, b), c)