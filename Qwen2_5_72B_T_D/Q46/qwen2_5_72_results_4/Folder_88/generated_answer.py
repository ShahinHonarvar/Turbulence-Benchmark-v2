from math import gcd

def gcf_three_nums(numbers):
    a = numbers[47]
    b = numbers[10]
    c = numbers[28]
    temp = gcd(a, b)
    result = gcd(temp, c)
    return result