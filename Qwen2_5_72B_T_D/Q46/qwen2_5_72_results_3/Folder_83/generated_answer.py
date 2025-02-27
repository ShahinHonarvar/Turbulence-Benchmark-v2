from math import gcd

def gcf_three_nums(numbers):
    a = numbers[56]
    b = numbers[54]
    c = numbers[13]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd