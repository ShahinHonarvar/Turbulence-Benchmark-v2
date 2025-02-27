from math import gcd

def gcf_three_nums(numbers):
    a = numbers[93]
    b = numbers[94]
    c = numbers[57]
    return gcd(gcd(a, b), c)