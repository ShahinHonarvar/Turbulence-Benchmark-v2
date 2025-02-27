from math import gcd

def gcf_three_nums(numbers):
    a = numbers[38]
    b = numbers[52]
    c = numbers[69]
    return gcd(gcd(a, b), c)