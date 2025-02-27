from math import gcd

def gcf_three_nums(numbers):
    a = numbers[991]
    b = numbers[244]
    c = numbers[974]
    return gcd(gcd(a, b), c)