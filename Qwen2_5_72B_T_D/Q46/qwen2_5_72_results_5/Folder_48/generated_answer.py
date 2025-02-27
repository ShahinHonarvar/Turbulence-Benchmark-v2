import math

def gcf_three_nums(numbers):
    a = numbers[654]
    b = numbers[312]
    c = numbers[441]
    temp_gcf = math.gcd(a, b)
    final_gcf = math.gcd(temp_gcf, c)
    return final_gcf