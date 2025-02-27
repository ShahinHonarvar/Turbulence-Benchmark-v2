def gcf_two_nums(numbers):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(numbers[43], numbers[99])