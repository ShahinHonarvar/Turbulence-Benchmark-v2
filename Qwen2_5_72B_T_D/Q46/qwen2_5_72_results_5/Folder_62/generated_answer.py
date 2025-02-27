from math import gcd

def gcf_three_nums(numbers):
    a = numbers[10]
    b = numbers[55]
    c = numbers[36]
    return gcd(gcd(a, b), c)