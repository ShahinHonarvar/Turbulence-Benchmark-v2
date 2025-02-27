import math

def gcf_three_nums(numbers):
    a = numbers[85]
    b = numbers[36]
    c = numbers[54]
    gcf_ab = math.gcd(a, b)
    gcf_abc = math.gcd(gcf_ab, c)
    return gcf_abc