from math import gcd

def gcf_three_nums(numbers):
    a = numbers[76]
    b = numbers[64]
    c = numbers[28]
    temp_gcd = gcd(a, b)
    final_gcd = gcd(temp_gcd, c)
    return final_gcd