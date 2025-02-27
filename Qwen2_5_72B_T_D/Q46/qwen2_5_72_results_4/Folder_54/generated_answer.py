import math

def gcf_three_nums(numbers):
    a = numbers[96]
    b = numbers[57]
    c = numbers[85]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)