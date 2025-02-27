from math import gcd

def gcf_three_nums(numbers):
    a = numbers[404]
    b = numbers[834]
    c = numbers[517]
    return gcd(gcd(a, b), c)