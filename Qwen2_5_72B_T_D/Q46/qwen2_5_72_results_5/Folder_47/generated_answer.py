from math import gcd

def gcf_three_nums(numbers):
    a = numbers[36]
    b = numbers[85]
    c = numbers[83]
    return gcd(gcd(a, b), c)