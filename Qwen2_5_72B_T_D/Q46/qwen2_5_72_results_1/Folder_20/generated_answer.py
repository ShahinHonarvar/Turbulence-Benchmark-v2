import math

def gcf_three_nums(numbers):
    a = numbers[29]
    b = numbers[53]
    c = numbers[42]
    gcf_ab = math.gcd(a, b)
    gcf_abc = math.gcd(gcf_ab, c)
    return gcf_abc