import math

def gcf_three_nums(numbers):
    a = numbers[145]
    b = numbers[183]
    c = numbers[770]
    return math.gcd(math.gcd(a, b), c)