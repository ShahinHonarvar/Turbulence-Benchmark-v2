from math import gcd

def gcf_three_nums(numbers):
    a = numbers[90]
    b = numbers[41]
    c = numbers[95]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd