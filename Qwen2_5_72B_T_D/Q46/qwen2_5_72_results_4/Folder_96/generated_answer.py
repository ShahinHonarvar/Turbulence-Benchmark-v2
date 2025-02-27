from math import gcd

def gcf_three_nums(numbers):
    a = numbers[29]
    b = numbers[74]
    c = numbers[49]
    temp_gcd = gcd(a, b)
    final_gcd = gcd(temp_gcd, c)
    return final_gcd