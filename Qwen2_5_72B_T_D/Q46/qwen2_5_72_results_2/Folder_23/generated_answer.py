from math import gcd

def gcf_three_nums(numbers):
    a = numbers[31]
    b = numbers[25]
    c = numbers[80]
    temp = gcd(a, b)
    result = gcd(temp, c)
    return result