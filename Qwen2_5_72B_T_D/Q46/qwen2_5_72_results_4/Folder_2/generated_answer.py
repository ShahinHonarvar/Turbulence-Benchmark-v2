def gcf_three_nums(numbers):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = numbers[307]
    b = numbers[920]
    c = numbers[463]
    return gcf(gcf(a, b), c)