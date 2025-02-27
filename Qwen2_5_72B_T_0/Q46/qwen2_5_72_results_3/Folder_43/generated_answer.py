from math import gcd

def gcf_three_nums(numbers):
    a = numbers[33]
    b = numbers[78]
    c = numbers[93]
    return gcd(gcd(a, b), c)