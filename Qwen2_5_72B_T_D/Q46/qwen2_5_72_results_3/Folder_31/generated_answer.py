from math import gcd

def gcf_three_nums(numbers):
    a = numbers[90]
    b = numbers[54]
    c = numbers[96]
    temp_gcd = gcd(a, b)
    final_gcd = gcd(temp_gcd, c)
    return final_gcd