from math import gcd

def gcf_three_nums(numbers):
    a = numbers[16]
    b = numbers[87]
    c = numbers[95]
    temp_gcd = gcd(a, b)
    result = gcd(temp_gcd, c)
    return result