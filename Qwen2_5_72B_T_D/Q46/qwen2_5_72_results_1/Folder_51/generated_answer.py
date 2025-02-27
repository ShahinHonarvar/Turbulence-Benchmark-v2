import math

def gcf_three_nums(numbers):
    a = numbers[21]
    b = numbers[69]
    c = numbers[41]
    return math.gcd(math.gcd(a, b), c)