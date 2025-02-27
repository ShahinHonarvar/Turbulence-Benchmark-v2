from math import gcd

def gcf_three_nums(numbers):
    a = numbers[20]
    b = numbers[17]
    c = numbers[28]
    temp = gcd(a, b)
    result = gcd(temp, c)
    return result