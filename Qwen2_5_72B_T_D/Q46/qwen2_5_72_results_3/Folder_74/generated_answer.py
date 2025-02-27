import math

def gcf_three_nums(numbers):
    a = numbers[99]
    b = numbers[95]
    c = numbers[80]
    return math.gcd(math.gcd(a, b), c)