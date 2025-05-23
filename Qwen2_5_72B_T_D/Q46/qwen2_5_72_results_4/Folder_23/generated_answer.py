from math import gcd

def gcf_three_nums(numbers):
    a = numbers[31]
    b = numbers[25]
    c = numbers[80]
    temp_gcd = gcd(a, b)
    final_gcd = gcd(temp_gcd, c)
    return final_gcd