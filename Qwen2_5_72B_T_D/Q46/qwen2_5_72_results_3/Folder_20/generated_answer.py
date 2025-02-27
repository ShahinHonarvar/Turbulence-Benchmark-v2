from math import gcd

def gcf_three_nums(numbers):
    a = numbers[29]
    b = numbers[53]
    c = numbers[42]
    return gcd(gcd(a, b), c)