def gcf_three_nums(numbers):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = numbers[91]
    num2 = numbers[45]
    num3 = numbers[48]
    result = gcf(gcf(num1, num2), num3)
    return result