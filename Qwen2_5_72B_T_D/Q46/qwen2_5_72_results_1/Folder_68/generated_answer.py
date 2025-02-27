from math import gcd

def gcf_three_nums(numbers):
    a = numbers[4]
    b = numbers[1]
    c = numbers[7]
    temp_gcd = gcd(a, b)
    final_gcd = gcd(temp_gcd, c)
    return final_gcd