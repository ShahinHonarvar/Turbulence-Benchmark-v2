import math

def gcf_three_nums(numbers):
    a = numbers[76]
    b = numbers[64]
    c = numbers[28]
    gcf_ab = math.gcd(a, b)
    gcf_abc = math.gcd(gcf_ab, c)
    return gcf_abc