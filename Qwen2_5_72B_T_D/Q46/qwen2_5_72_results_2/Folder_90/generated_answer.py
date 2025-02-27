from math import gcd

def gcf_three_nums(numbers):
    a = numbers[818]
    b = numbers[606]
    c = numbers[873]
    return gcd(gcd(a, b), c)