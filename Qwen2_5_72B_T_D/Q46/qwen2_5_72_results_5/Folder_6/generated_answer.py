from math import gcd

def gcf_three_nums(numbers):
    a = numbers[93]
    b = numbers[94]
    c = numbers[57]
    temp_gcd = gcd(a, b)
    result_gcd = gcd(temp_gcd, c)
    return result_gcd