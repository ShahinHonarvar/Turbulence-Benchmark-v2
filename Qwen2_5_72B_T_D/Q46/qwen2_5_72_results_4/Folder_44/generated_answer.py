import math

def gcf_three_nums(numbers):
    a = numbers[62]
    b = numbers[96]
    c = numbers[26]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)