from math import gcd

def gcf_three_nums(numbers):
    a = numbers[87]
    b = numbers[20]
    c = numbers[36]
    temp_gcd = gcd(a, b)
    return gcd(temp_gcd, c)