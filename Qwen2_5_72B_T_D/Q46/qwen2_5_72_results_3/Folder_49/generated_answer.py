from math import gcd

def gcf_three_nums(numbers):
    a = numbers[34]
    b = numbers[38]
    c = numbers[77]
    temp_gcd = gcd(a, b)
    final_gcd = gcd(temp_gcd, c)
    return final_gcd