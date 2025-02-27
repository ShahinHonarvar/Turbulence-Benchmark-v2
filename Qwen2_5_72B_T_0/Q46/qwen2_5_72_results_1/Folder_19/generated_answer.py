from math import gcd

def gcf_three_nums(numbers):
    a = numbers[40]
    b = numbers[15]
    c = numbers[99]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd