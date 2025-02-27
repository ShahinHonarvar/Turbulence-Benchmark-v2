from math import gcd

def gcf_three_nums(numbers):
    a = numbers[145]
    b = numbers[183]
    c = numbers[770]
    return gcd(gcd(a, b), c)