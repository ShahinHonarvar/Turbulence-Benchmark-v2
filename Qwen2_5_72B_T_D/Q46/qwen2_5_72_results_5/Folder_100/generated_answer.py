from math import gcd

def gcf_three_nums(numbers):
    a = numbers[21]
    b = numbers[51]
    c = numbers[33]
    temp_gcd = gcd(a, b)
    result = gcd(temp_gcd, c)
    return result