from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[92]
    num2 = numbers[69]
    num3 = numbers[95]
    result = gcd(gcd(num1, num2), num3)
    return result