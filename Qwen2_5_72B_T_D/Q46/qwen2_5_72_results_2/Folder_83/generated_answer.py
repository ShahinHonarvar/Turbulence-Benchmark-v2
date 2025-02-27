import math

def gcf_three_nums(numbers):
    a = numbers[56]
    b = numbers[54]
    c = numbers[13]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)