import math

def gcf_three_nums(numbers):
    a = numbers[17]
    b = numbers[88]
    c = numbers[35]
    gcf_ab = math.gcd(a, b)
    gcf_abc = math.gcd(gcf_ab, c)
    return gcf_abc