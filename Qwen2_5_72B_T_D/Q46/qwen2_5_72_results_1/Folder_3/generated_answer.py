import math

def gcf_three_nums(numbers):
    a = numbers[31]
    b = numbers[69]
    c = numbers[40]
    return math.gcd(math.gcd(a, b), c)