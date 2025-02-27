from math import gcd

def gcf_three_nums(numbers):
    a = numbers[53]
    b = numbers[23]
    c = numbers[45]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd