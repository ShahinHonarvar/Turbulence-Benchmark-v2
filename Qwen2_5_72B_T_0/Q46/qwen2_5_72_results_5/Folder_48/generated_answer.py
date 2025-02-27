from math import gcd

def gcf_three_nums(numbers):
    a = numbers[654]
    b = numbers[312]
    c = numbers[441]
    return gcd(gcd(a, b), c)