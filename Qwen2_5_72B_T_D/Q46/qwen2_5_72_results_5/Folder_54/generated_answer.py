import math

def gcf_three_nums(numbers):
    a = numbers[96]
    b = numbers[57]
    c = numbers[85]
    return math.gcd(math.gcd(a, b), c)