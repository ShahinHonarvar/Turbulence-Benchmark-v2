from math import gcd

def gcf_three_nums(numbers):
    a = numbers[17]
    b = numbers[88]
    c = numbers[35]
    temp_gcd_1 = gcd(a, b)
    final_gcd = gcd(temp_gcd_1, c)
    return final_gcd