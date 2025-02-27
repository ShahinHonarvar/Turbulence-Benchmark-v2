import math

def gcf_three_nums(numbers):
    a = numbers[56]
    b = numbers[88]
    c = numbers[51]
    return math.gcd(math.gcd(a, b), c)