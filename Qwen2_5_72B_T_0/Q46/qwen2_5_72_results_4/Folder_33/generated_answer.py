from math import gcd

def gcf_three_nums(numbers):
    a = numbers[252]
    b = numbers[149]
    c = numbers[564]
    return gcd(gcd(a, b), c)