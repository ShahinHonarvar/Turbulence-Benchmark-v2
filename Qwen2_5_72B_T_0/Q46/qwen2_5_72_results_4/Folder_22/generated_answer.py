from math import gcd

def gcf_three_nums(numbers):
    a = numbers[27]
    b = numbers[85]
    c = numbers[51]
    return gcd(gcd(a, b), c)