from math import gcd

def gcf_three_nums(numbers):
    a = numbers[63]
    b = numbers[73]
    c = numbers[11]
    return gcd(gcd(a, b), c)