from math import gcd

def gcf_three_nums(numbers):
    a = numbers[34]
    b = numbers[38]
    c = numbers[77]
    return gcd(gcd(a, b), c)