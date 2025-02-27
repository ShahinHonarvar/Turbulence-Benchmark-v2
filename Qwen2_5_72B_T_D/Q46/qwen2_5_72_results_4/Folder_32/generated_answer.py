import math

def gcf_three_nums(numbers):
    a = numbers[20]
    b = numbers[43]
    c = numbers[95]
    gcf_ab = math.gcd(a, b)
    gcf_abc = math.gcd(gcf_ab, c)
    return gcf_abc