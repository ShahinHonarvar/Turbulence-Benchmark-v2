from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[70]
    num2 = numbers[98]
    num3 = numbers[22]
    return gcd(gcd(num1, num2), num3)