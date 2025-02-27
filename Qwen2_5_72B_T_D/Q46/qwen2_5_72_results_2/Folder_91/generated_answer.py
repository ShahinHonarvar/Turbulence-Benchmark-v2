from math import gcd

def gcf_three_nums(numbers):
    a = numbers[3]
    b = numbers[8]
    c = numbers[9]
    temp_gcd = gcd(a, b)
    final_gcd = gcd(temp_gcd, c)
    return final_gcd