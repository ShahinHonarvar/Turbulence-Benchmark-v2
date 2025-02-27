import math

def gcf_three_nums(numbers):
    a = numbers[41]
    b = numbers[69]
    c = numbers[28]
    return math.gcd(math.gcd(a, b), c)