from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[99]
    num2 = numbers[63]
    num3 = numbers[74]
    result = gcd(gcd(num1, num2), num3)
    return result