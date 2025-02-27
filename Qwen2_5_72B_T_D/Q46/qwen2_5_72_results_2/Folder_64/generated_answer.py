import math

def gcf_three_nums(numbers):
    a = numbers[0]
    b = numbers[3]
    c = numbers[8]
    return math.gcd(math.gcd(a, b), c)