import math

def gcf_three_nums(numbers):
    num1 = numbers[18]
    num2 = numbers[37]
    num3 = numbers[43]
    return math.gcd(math.gcd(num1, num2), num3)