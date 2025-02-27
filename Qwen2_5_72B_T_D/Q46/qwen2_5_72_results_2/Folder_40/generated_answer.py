import math

def gcf_three_nums(numbers):
    a = numbers[1]
    b = numbers[6]
    c = numbers[8]
    return math.gcd(math.gcd(a, b), c)