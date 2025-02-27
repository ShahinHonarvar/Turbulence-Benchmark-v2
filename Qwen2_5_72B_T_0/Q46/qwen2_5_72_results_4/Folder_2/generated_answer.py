from math import gcd

def gcf_three_nums(numbers):
    a = numbers[307]
    b = numbers[920]
    c = numbers[463]
    return gcd(gcd(a, b), c)