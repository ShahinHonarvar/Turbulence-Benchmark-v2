from math import gcd

def gcf_three_nums(numbers):
    a = numbers[637]
    b = numbers[411]
    c = numbers[757]
    return gcd(gcd(a, b), c)