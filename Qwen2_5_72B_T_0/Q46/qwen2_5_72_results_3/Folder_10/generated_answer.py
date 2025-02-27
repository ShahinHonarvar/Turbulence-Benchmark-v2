from math import gcd

def gcf_three_nums(numbers):
    a = numbers[86]
    b = numbers[89]
    c = numbers[49]
    return gcd(gcd(a, b), c)