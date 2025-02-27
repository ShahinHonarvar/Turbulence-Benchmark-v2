from math import gcd

def gcf_three_nums(numbers):
    a = numbers[14]
    b = numbers[21]
    c = numbers[17]
    temp = gcd(a, b)
    result = gcd(temp, c)
    return result