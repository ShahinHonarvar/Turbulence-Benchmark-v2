import math

def gcf_three_nums(numbers):
    a = numbers[90]
    b = numbers[84]
    c = numbers[47]
    return math.gcd(math.gcd(a, b), c)