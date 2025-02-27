from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[36]
    num2 = numbers[85]
    num3 = numbers[83]
    result = gcd(gcd(num1, num2), num3)
    return result