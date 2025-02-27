from math import gcd

def gcf_three_nums(numbers):
    a = numbers[20]
    b = numbers[17]
    c = numbers[28]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd