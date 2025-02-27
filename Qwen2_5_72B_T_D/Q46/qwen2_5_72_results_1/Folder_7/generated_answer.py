from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[477]
    num2 = numbers[696]
    num3 = numbers[663]
    result = gcd(gcd(num1, num2), num3)
    return result