from math import gcd

def gcf_three_nums(numbers):
    a = numbers[66]
    b = numbers[56]
    c = numbers[92]
    return gcd(gcd(a, b), c)