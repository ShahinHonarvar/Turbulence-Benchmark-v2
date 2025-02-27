from math import gcd

def gcf_three_nums(numbers):
    a = numbers[92]
    b = numbers[69]
    c = numbers[95]
    return gcd(gcd(a, b), c)