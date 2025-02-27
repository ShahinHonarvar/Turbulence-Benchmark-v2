def gcf_three_nums(numbers):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = numbers[477]
    b = numbers[696]
    c = numbers[663]
    return gcf(gcf(a, b), c)