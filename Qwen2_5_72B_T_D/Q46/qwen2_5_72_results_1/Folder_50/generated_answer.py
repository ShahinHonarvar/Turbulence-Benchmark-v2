import math

def gcf_three_nums(numbers):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (numbers[20], numbers[35], numbers[74])
    return gcf(gcf(a, b), c)