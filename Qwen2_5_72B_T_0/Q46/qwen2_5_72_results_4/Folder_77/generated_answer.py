from math import gcd

def gcf_three_nums(numbers):
    a = numbers[693]
    b = numbers[331]
    c = numbers[668]
    return gcd(gcd(a, b), c)