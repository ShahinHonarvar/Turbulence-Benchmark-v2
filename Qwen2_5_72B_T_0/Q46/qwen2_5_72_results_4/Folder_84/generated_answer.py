from math import gcd

def gcf_three_nums(numbers):
    a = numbers[695]
    b = numbers[710]
    c = numbers[914]
    return gcd(gcd(a, b), c)