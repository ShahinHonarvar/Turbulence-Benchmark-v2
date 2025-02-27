from math import gcd

def gcf_three_nums(numbers):
    a = numbers[74]
    b = numbers[60]
    c = numbers[28]
    temp = gcd(a, b)
    result = gcd(temp, c)
    return result