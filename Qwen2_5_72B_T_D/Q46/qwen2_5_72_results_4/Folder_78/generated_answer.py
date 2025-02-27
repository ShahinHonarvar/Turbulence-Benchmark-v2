from math import gcd

def gcf_three_nums(numbers):

    def find_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = numbers[13]
    num2 = numbers[70]
    num3 = numbers[32]
    result = gcd(gcd(num1, num2), num3)
    return result