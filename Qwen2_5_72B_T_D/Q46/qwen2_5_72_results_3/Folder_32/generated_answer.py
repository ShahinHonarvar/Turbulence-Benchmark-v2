import math

def gcf_three_nums(numbers):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(gcf(numbers[20], numbers[43]), numbers[95])