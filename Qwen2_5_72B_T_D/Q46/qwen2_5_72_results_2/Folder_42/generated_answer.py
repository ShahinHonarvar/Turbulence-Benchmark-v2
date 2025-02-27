from math import gcd

def gcf_three_nums(numbers):
    a = numbers[19]
    b = numbers[69]
    c = numbers[97]
    return gcd(gcd(a, b), c)