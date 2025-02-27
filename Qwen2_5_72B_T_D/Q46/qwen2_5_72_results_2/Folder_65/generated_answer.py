from math import gcd

def gcf_three_nums(numbers):
    a = numbers[76]
    b = numbers[18]
    c = numbers[10]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd