from math import gcd

def gcf_three_nums(numbers):
    a = numbers[558]
    b = numbers[110]
    c = numbers[628]
    return gcd(gcd(a, b), c)