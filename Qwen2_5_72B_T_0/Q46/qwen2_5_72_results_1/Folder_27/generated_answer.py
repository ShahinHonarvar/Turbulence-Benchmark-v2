from math import gcd

def gcf_three_nums(numbers):
    a = numbers[76]
    b = numbers[64]
    c = numbers[28]
    temp = gcd(a, b)
    result = gcd(temp, c)
    return result