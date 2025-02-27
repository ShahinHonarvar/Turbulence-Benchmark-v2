from math import gcd

def gcf_three_nums(numbers):
    a = numbers[27]
    b = numbers[51]
    c = numbers[74]
    return gcd(gcd(a, b), c)