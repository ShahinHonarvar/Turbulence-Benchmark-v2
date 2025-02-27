from math import gcd

def gcf_three_nums(numbers):
    a = numbers[19]
    b = numbers[94]
    c = numbers[78]
    return gcd(gcd(a, b), c)