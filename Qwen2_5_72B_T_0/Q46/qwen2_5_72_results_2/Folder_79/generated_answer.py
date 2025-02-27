from math import gcd

def gcf_three_nums(numbers):
    a = numbers[16]
    b = numbers[87]
    c = numbers[95]
    return gcd(gcd(a, b), c)