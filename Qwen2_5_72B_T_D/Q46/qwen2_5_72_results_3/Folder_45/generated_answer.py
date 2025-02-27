import math

def gcf_three_nums(numbers):
    a = numbers[23]
    b = numbers[46]
    c = numbers[84]
    return math.gcd(math.gcd(a, b), c)