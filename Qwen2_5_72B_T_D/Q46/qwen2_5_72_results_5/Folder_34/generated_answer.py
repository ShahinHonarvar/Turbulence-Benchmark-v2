from math import gcd

def gcf_three_nums(numbers):
    a = numbers[53]
    b = numbers[23]
    c = numbers[45]
    temp = gcd(a, b)
    result = gcd(temp, c)
    return result