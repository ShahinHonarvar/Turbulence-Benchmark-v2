from math import gcd

def gcf_three_nums(numbers):
    a = numbers[8]
    b = numbers[2]
    c = numbers[1]
    temp_gcd = gcd(a, b)
    final_gcd = gcd(temp_gcd, c)
    return final_gcd