import math

def gcf_three_nums(numbers):
    a = numbers[66]
    b = numbers[56]
    c = numbers[92]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)