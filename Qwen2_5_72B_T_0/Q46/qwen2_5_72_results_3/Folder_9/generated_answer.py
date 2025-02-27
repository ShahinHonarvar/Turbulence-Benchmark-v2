from math import gcd

def gcf_three_nums(numbers):
    a = numbers[66]
    b = numbers[90]
    c = numbers[27]
    return gcd(gcd(a, b), c)