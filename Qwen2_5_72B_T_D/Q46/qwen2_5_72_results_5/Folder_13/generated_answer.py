import math

def gcf_three_nums(numbers):
    a = numbers[991]
    b = numbers[244]
    c = numbers[974]
    return math.gcd(math.gcd(a, b), c)