from math import gcd

def gcf_three_nums(numbers):
    a = numbers[990]
    b = numbers[671]
    c = numbers[711]
    return gcd(gcd(a, b), c)