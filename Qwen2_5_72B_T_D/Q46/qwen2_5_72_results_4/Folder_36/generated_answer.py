from math import gcd

def gcf_three_nums(numbers):
    a = numbers[427]
    b = numbers[761]
    c = numbers[148]
    return gcd(gcd(a, b), c)