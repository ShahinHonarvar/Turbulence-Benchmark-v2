from math import gcd

def gcf_three_nums(numbers):
    a = numbers[10]
    b = numbers[55]
    c = numbers[36]
    temp_gcd = gcd(a, b)
    final_gcd = gcd(temp_gcd, c)
    return final_gcd