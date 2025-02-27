from math import gcd

def gcf_three_nums(numbers):
    a = numbers[0]
    b = numbers[4]
    c = numbers[8]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd