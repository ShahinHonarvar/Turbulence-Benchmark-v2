import math

def gcf_three_nums(numbers):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = numbers[14]
    num2 = numbers[21]
    num3 = numbers[17]
    result = gcf(gcf(num1, num2), num3)
    return result