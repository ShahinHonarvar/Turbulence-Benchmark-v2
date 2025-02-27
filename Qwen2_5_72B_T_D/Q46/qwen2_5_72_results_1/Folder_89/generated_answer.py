import math

def gcf_three_nums(numbers):
    a = numbers[63]
    b = numbers[73]
    c = numbers[11]
    gcf_ab = math.gcd(a, b)
    return math.gcd(gcf_ab, c)