import math

def gcf_three_nums(numbers):
    a = numbers[76]
    b = numbers[35]
    c = numbers[74]
    return math.gcd(math.gcd(a, b), c)