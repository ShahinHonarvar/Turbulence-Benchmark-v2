import math

def gcf_three_nums(numbers):
    a = numbers[91]
    b = numbers[45]
    c = numbers[48]
    return math.gcd(math.gcd(a, b), c)