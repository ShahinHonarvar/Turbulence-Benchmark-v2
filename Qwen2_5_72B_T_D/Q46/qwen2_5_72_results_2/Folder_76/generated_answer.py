def gcf_three_nums(numbers):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(gcf(numbers[876], numbers[203]), numbers[100])