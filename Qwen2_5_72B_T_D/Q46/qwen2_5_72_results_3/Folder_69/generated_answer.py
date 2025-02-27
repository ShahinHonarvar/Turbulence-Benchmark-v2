import math

def gcf_three_nums(numbers):
    a = numbers[404]
    b = numbers[834]
    c = numbers[517]
    return math.gcd(math.gcd(a, b), c)